import threading

import rospy

from dialogue import Dialogue


class DialogueManager:
    """
    A DialogueManager is used to manage Dialogues.
    """

    def __init__(self, dialogue_library):
        # type: (DialogueLibrary) -> DialogueManager
        """
        DialogueManager constructor.
        :param dialogue_library: The DialogueLibrary to use to convert topics into Dialogues.
        """
        self.dialogue_library = dialogue_library
        self.current_dialogue = None
        self.current_topic = None
        self.topics = {}

        self.running = False
        self.switching_topic = False
        self.should_interrupt = False

        self.__add_topic_event = threading.Event()

    def start(self, utter, threaded=False, perpetual=True):
        # type: (Callable[str, None], bool, bool) -> None
        """
        Start the DialogueManager. This uses the DialogueLibrary to go through every dialogue in the
        topics dict, based on their priority (high priority first). This can be run either synchronously or
        asynchronously (in a new thread).
        :param utter: The function that can be called to utter a sentence.
        :param threaded: Whether to run the DialogueManager in a different thread.
        :param perpetual: Whether to stop running the DialogueManager after all dialogues are done.
        """
        self.running = True

        if threaded:
            thread = threading.Thread(target=self.__start_worker(utter, perpetual))
            thread.daemon = True
            thread.start()
        else:
            self.__start_worker(utter, perpetual)

    def __start_worker(self, utter, perpetual):
        # type: (Callable[str, None], bool) -> None
        """
        The worker function for start(). This is a seperate function to ease threading.
        :param utter: The function that can be called to utter a sentence.
        """
        rospy.loginfo("Starting DialogueManager worker{}".format(" in perpetual mode.." if perpetual else ".."))

        while not self.should_interrupt:
            while len(self.topics) > 0:
                rospy.loginfo("Selecting new topic to talk about..")

                self.current_topic = self.__get_next_current_topic()
                self.current_dialogue = self.dialogue_library.get_dialogue_for_topic(self.current_topic)

                self.switching_topic = False

                rospy.loginfo("New topic: {}".format(self.current_topic))

                while self.current_dialogue.dialogue_remaining():
                    if self.switching_topic or self.should_interrupt:
                        rospy.loginfo("Canceling dialogue about {}..".format(self.current_topic))
                        self.current_dialogue.cancel_dialogue()

                    self.current_dialogue.proceed_dialogue(utter)

                rospy.loginfo("Dialogue about {} finished.".format(self.current_topic))

                self.__delete_topic(self.current_topic)

            if perpetual and not self.should_interrupt:
                rospy.loginfo("DialogueManager seems to be done talking. Waiting for more topics to talk about...")

                self.__add_topic_event.wait(timeout=None)
                self.__add_topic_event.clear()

            else:
                rospy.loginfo("DialogueManager is done talking. Stopping..")
                self.__cleanup()

    def stop(self, force=False):
        # type: () -> None
        """
        Request the DialogueManager to stop. This will continue the dialogue until the next point where the dialogue can
        be cancelled.
        :param force: If this is true, don't wait for the conversation to finish.
        """
        rospy.loginfo("DialogueManager received stop request.")
        self.should_interrupt = True

        if force:
            self.__cleanup()
            self.topics = {}

    def __cleanup(self):
        # type: () -> None
        """
        Clean up the class variables after stopping.
        """
        rospy.loginfo("DialogueManager cleaning up..")
        self.current_dialogue = None
        self.switching_topic = False
        self.should_interrupt = False
        self.current_topic = None
        self.running = False

    def add_topic(self, topic, priority):
        # type: (str, float) -> None
        """
        Add a topic with a priority to the DialogueManager. This can be called before or
        after starting the start method.
        :param topic: The topic to add.
        :param priority: The priority to assign this topic.
        """
        rospy.loginfo("Adding {} to the topic list with priority {}..".format(topic, priority))

        self.topics[priority] = topic

        if self.running and self.__get_next_current_topic() == topic:
            rospy.loginfo("{} is the highest priority ({}) topic. Requesting topic switch...".format(topic, priority))
            self.switching_topic = True

        self.__add_topic_event.set()

    def remove_topic(self, topic):
        # type: (str) -> None
        """
        Remove a topic from the dialogue manager. This can be used before and after starting the dialogue manager.
        :param topic: The topic to remove.
        """
        rospy.loginfo("Removing {} from the topic list..".format(topic))

        if self.running and self.current_topic == topic:
            rospy.loginfo("{} is the current topic while we are trying to remove it. Requesting change of topic before removal...".format(topic))

            self.switching_topic = True
        else:
            self.__delete_topic(topic)

    def has_topic(self, topic):
        # type: (str) -> bool
        """
        Whether this topic is already in the list of topics to be talked about.
        :param topic: The topic to check
        :return: Whether _topic_ is in the list of topics for this DialogueManager
        """
        for key, val in self.topics.iteritems():
            if val == topic:
                return True

        return False

    def __get_next_current_topic(self):
        # type: () -> str
        """
        Get the topic from self.topics with the highest priority.
        :return: The topic with the highest priority.
        """
        return self.topics[sorted(self.topics.iterkeys())[0]]

    def __delete_topic(self, topic):
        # type: (str) -> None
        """
        Removes a topic from the self.topics dict.
        :param topic: The topic to remove
        """
        rospy.loginfo("Deleting {} from the topic list.".format(topic))

        for key, val in self.topics.iteritems():
            if val == topic:
                del self.topics[key]
                break


class DialogueLibrary:

    def get_dialogue_for_topic(self, topic):
        # type: (str) -> Dialogue
        """
        Returns a dialogue that can be used to talk about the topic.
        :param topic: The topic to retrieve a dialogue about.
        :return: A dialogue about the requested topic.
        """
        raise NotImplementedError

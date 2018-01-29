import threading
import time

import rospy
from typing import List, Union

from dialogue import Dialogue


class DialogueManager:
    """
    A DialogueManager is used to manage Dialogues.
    """

    def __init__(self, dialogue_library, fallback_dialogue=None):
        # type: (DialogueLibrary, Dialogue) -> self
        """
        DialogueManager constructor.
        :param dialogue_library: The DialogueLibrary to use to convert topics into Dialogues.
        :param fallback_dialogue: The Dialogue to use when there are no topics left. Usually a chatbot dialogue
            If None, dialogue will stop after running out of topics.
        """
        self.dialogue_library = dialogue_library  # type: DialogueLibrary
        self.current_dialogue = None  # type: Dialogue
        self.current_topic = None  # type: DialogueTopic
        self.topics = []  # type: List[DialogueTopic]

        self.running = False
        self.switching_topic = False
        self.should_interrupt = False

        self.fallback_dialogue = fallback_dialogue

        self.topic_history = []  # type: List[DialogueTopic]

    def start(self, threaded=False):
        # type: (bool) -> None
        """
        Start the DialogueManager. This uses the DialogueLibrary to go through every dialogue in the
        topics dict, based on their priority (high priority first). This can be run either synchronously or
        asynchronously (in a new thread).
        :param threaded: Whether to run the DialogueManager in a different thread.
        """
        self.running = True

        rospy.loginfo("Starting Dialogue Manager in {} mode.".format("threaded" if threaded else "non-threaded"))

        rospy.on_shutdown(self.force_stop)

        if threaded:
            thread = threading.Thread(target=self.__start_worker())
            thread.daemon = True
            thread.start()
        else:
            self.__start_worker()

    def __start_worker(self):
        # type: () -> None
        """
        The worker function for start(). This is a separate function to ease threading.
        """
        rospy.loginfo("Starting DialogueManager worker...")

        rospy.loginfo("Sleeping DialogueManager worker for 5 seconds...")

        time.sleep(5)

        rate = rospy.Rate(2)

        while not self.should_interrupt:
            self.__talk()

            self.__talk_fallback()

            rate.sleep()

    def __talk(self):
        while len(self.topics) > 0:
            rospy.loginfo("Selecting new topic to talk about..")

            self.current_topic = self.__get_next_current_topic()
            self.current_dialogue = self.dialogue_library.get_dialogue_for_topic(self.current_topic.label)

            self.switching_topic = False

            rospy.loginfo("New topic: {}".format(self.current_topic.label))

            self.topic_history.append(self.current_topic)

            while self.current_dialogue.dialogue_remaining():
                if self.should_interrupt:
                    return

                if self.switching_topic or self.should_interrupt:
                    rospy.loginfo("Canceling dialogue about {}..".format(self.current_topic.label))
                    self.current_dialogue.cancel_dialogue(self.__get_next_current_topic())

                self.decrease_current_topic_priority()

                self.current_dialogue.proceed_dialogue(self.current_topic.topic_id)

            rospy.loginfo("Dialogue about {} finished.".format(self.current_topic.label))

            self.__delete_topic(self.current_topic)

    def __talk_fallback(self):
        if self.fallback_dialogue is not None and not self.should_interrupt:
            rospy.loginfo("DialogueManager seems to be done talking. Starting Chatbot conversation...")

            self.fallback_dialogue.is_canceled = False
            self.fallback_dialogue.should_cancel = False

            while self.fallback_dialogue.dialogue_remaining():
                if rospy.is_shutdown():
                    return

                if self.switching_topic or self.should_interrupt:
                    rospy.loginfo(
                        "Canceling fallback dialogue in favor of {}..".format(self.__get_next_current_topic().label))
                    self.fallback_dialogue.cancel_dialogue(self.__get_next_current_topic())

                self.fallback_dialogue.proceed_dialogue(self.current_topic.topic_id)

            rospy.loginfo(
                "The fallback dialogue has run out!")  # maybe do something here? it shouldn't happen with mitsuku, but ..

        else:
            rospy.loginfo("DialogueManager is done talking. Waiting for new subjects.")

    def force_stop(self):
        self.stop(True)

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
            rospy.loginfo("DialogueManager forcing stop.")
            self.__cleanup()
            self.topics = []

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

    def add_topic(self, topic, topic_id, priority):
        # type: (str, str, float) -> None
        """
        Add a topic with a priority to the DialogueManager. This can be called before or
        after starting the start method.
        :param topic: The topic to add.
        :param topic_id: The id of the topic.
        :param priority: The priority of the topic.
        """
        t = DialogueTopic(priority, topic_id, topic)

        if self.has_topic(topic):
            rospy.logdebug("Trying to add {} to the topics, but a topic with that label already exists! Skipping..".format(topic))
            return

        rospy.loginfo("Adding {} to the topic list with priority {}..".format(topic, priority))

        self.topics.append(t)

        if self.running and self.__get_next_current_topic() == t:
            rospy.loginfo("{} is the highest priority ({}) topic. Requesting topic switch...".format(topic, priority))
            self.switching_topic = True

    def decrease_current_topic_priority(self):
        """
        Decreases the current_topic's priority. We want the conversation to interrupt for more recent topics, so
        we decrease the priority of the current topic the longer we talk about it.
        """
        if self.current_topic is not None:
            priority = self.current_topic.priority

            priority -= 0.1

            if priority < 0:
                priority = 0

            self.current_topic.priority = priority
            self.topics[self.topics.index(self.current_topic)].priority = priority

            if self.running and self.__get_next_current_topic() != self.current_topic:
                rospy.loginfo("{} is not the highest priority ({}) topic anymore. Requesting topic switch...".format(self.current_topic.label, priority))
                self.switching_topic = True

    def remove_topic(self, topic):
        # type: (str) -> None
        """
        Remove a topic from the dialogue manager. This can be used before and after starting the dialogue manager.
        :param topic: The topic to remove.
        """
        rospy.loginfo("Removing {} from the topic list..".format(topic))

        if self.running and self.current_topic.label == topic:
            rospy.loginfo("{} is the current topic while we are trying to remove it. Requesting change of topic before removal...".format(topic))

            self.switching_topic = True
        else:
            self.__delete_topics_with_label(topic)

    def has_topic(self, topic):
        # type: (str) -> bool
        """
        Whether this topic is already in the list of topics to be talked about.
        :param topic: The topic to check
        :return: Whether topic is in the list of topics for this DialogueManager
        """
        for t in self.topics:
            if t.label == topic:
                return True

        return False

    def __get_next_current_topic(self):
        # type: () -> Union[DialogueTopic, None]
        """
        Get the topic from self.topics with the highest priority.
        :return: The topic with the highest priority.
        """
        if len(self.topics) != 0:
            self.topics.sort(key=lambda t: t.priority, reverse=True)

            return self.topics[0]

        return None

    def __delete_topics_with_label(self, topic_label):
        # type: (str) -> None
        """
        Removes a topic from the self.topics list.
        :param topic_label: The label of the topic to remove
        """
        rospy.loginfo("Deleting {} from the topic list.".format(topic_label))

        for topic in self.topics:
            if topic.label == topic_label:
                self.topics.remove(topic)

    def __delete_topic(self, topic):
        # type: (DialogueTopic) -> None
        """
        Removes a topic from the self.topics list.
        :param topic: The topic to remove
        """
        rospy.loginfo("Deleting {} from the topic list.".format(topic.label))

        self.topics.remove(topic)

    def get_topic_history(self):
        # type: () -> list[str]
        """
        Get the topic history for this dialogue manager. This contains all topics have been, or are, talked about.
        :return: All topics talked about in the past and the current topic.
        """

        topic_history_labels = []

        for topic in self.topic_history:
            topic_history_labels.append(topic.label)

        return topic_history_labels

    def __dummy_callback(self, data):
        pass


class DialogueTopic:
    def __init__(self, priority, topic_id, label):
        # type: (float, str) -> self
        self.label = label
        self.topic_id = topic_id
        self.priority = priority


class DialogueLibrary:

    def get_dialogue_for_topic(self, topic):
        # type: (str) -> Dialogue
        """
        Returns a dialogue that can be used to talk about the topic.
        :param topic: The topic to retrieve a dialogue about.
        :return: A dialogue about the requested topic.
        """
        raise NotImplementedError

import rospy
from look_helper.srv import SetLookAtTarget
from typing import Union

from __init__ import *


class DialogueActionLook(AbstractDialogueAction):
    """
    DialogueActionLook tells the robot to look at a specified object.
    """

    LOOK_TYPE_WATCH_ENVIRONMENT = 0
    LOOK_TYPE_WATCH_CONVERSATION_PARTNER = 1
    LOOK_TYPE_WATCH_CONVERSATION_TOPIC = 2

    def __init__(self, look_type, cancelable, next_action):
        # type: (int, bool, Union[AbstractDialogueAction, None]) -> None
        """
        Initializes the DialogueLookAction
        :param look_type: An integer indicating what the robot should look at. See various LOOK_TYPE_WATCH_* variables
            for possible values. If a value is invalid, the default look_type is to watch the environment.
        :param cancelable: Whether the dialogue can be cancelled after this action.
        :param next_action: The next action in this dialogue.
        """
        self.look_type = look_type
        self.cancelable = cancelable
        self.next_action = next_action

    def run(self, tf):
        # type: (str) -> AbstractDialogueAction
        """
        Use this function to perform an action and return the next action. Return None when there is no next action.
        :param tf: The name of the tf2_ros transform of the object that is currently being talked about.
        :return: The next action in the Dialogue. Return None when there is no next action.
        """

        # Python doesn't have a switch statement? Really?
        switch_dict = {
            self.LOOK_TYPE_WATCH_ENVIRONMENT: None,
            self.LOOK_TYPE_WATCH_CONVERSATION_PARTNER: "person",
            self.LOOK_TYPE_WATCH_CONVERSATION_TOPIC: tf
        }

        self.set_look_target(switch_dict.get(self.look_type, None))

        return self.next_action

    def can_cancel(self):
        # type () -> bool
        """
        Whether the Dialogue can logically be cancelled after this DialogueAction.
        :return: Is this a good place in the Dialogue to stop if the Dialogue has to be cancelled?
        """
        return self.cancelable

    @staticmethod
    def set_look_target(target_tf_name):
        # type: (str) -> bool
        """
        This function calls the `look_helper/look_target` service, to change the object the robot looks at.
        :param target_tf_name: The name of the tf of the object to look at. None to watch environment randomly.
        :return: Whether the request succeeded.
        """
        service_name = 'look_helper/look_target'

        rospy.wait_for_service(service_name)

        try:
            rospy.loginfo("Setting look target to {}.".format(target_tf_name))

            set_look_at_target = rospy.ServiceProxy(service_name, SetLookAtTarget)

            return set_look_at_target(target_tf_name)
        except rospy.ServiceException, e:
            print "Service call failed: %s" % e
            raise

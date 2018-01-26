import rospy
from commu_wrapper.srv import CommUUtter

from abstract_dialogue_action import AbstractDialogueAction


class AbstractDialogueActionTalk(AbstractDialogueAction):
    """
    AbstractDialogueActionTalk defines an abstract super-class for a DialogueAction which
     makes the robot utter and allows for optional user input.
    """

    def run(self, tf):
        # type: (str) -> AbstractDialogueAction
        """
        Use this function to perform an action and return the next action. Return None when there is no next action.
        :param tf: The name of the tf2_ros transform of the object that is currently being talked about.
        :return: The next action in the Dialogue. Return None when there is no next action.
        """
        raise NotImplementedError

    def can_cancel(self):
        # type () -> bool
        """
        Whether the Dialogue can logically be cancelled after this DialogueAction.
        :return: Is this a good place in the Dialogue to stop if the Dialogue has to be cancelled?
        """
        raise NotImplementedError

    @staticmethod
    def utter(utterance):
        # type: (str) -> bool
        """
        Call the CommUUtter service to make the CommU/Sota utter the specified utterance.
        :param utterance: The string to utter.
        :return: Whether the robot received the utterance successfully.
        """
        service_name = '/commu_wrapper/utter'

        rospy.wait_for_service(service_name)

        try:
            utter_srv = rospy.ServiceProxy(service_name, CommUUtter)

            rospy.loginfo("Uttering: " + str(utterance))

            if utterance is not None:
                success = utter_srv(utterance, True, True)

                rospy.loginfo("Uttering " + ("succeeded" if success else "failed!"))

                return success
            return True

        except rospy.ServiceException, e:
            print("Service call failed: %s" % e)
            raise

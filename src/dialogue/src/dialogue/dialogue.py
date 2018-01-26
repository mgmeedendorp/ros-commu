import rospy

from dialogue_action import *


class Dialogue:
    """
    A Dialogue represents a conversation between CommU and a human as seen from CommU. The conversation structure is
    defined by an AbstractDialogueAction.
    """

    def __init__(self, dialogue_root):
        # type: (AbstractDialogueAction) -> None
        """
        :param dialogue_root: The first action of the conversation.
        """
        self.dialogue_root = dialogue_root
        self.current_action = dialogue_root
        self.should_cancel = False
        self.is_canceled = False

    def proceed_dialogue(self, tf_talking_about=None):
        # type: (str) -> bool
        """
        Proceed the dialogue to the next action.
        :param tf_talking_about: The transform that is being talked about. None if this does not apply.
        :return: Whether the dialogue was proceeded.
        """
        if not self.dialogue_remaining():
            return False

        next_action = self.current_action.run(tf_talking_about)

        if self.should_cancel and self.current_action.can_cancel():
            rospy.loginfo("Dialogue cancelled.")
            self.is_canceled = True

        self.current_action = next_action

        return True

    def dialogue_remaining(self):
        # type: () -> bool
        """
        Checks whether the dialogue is finished.
        :return: Whether there is a next action in the dialogue.
        """
        return self.current_action is not None and not self.is_canceled

    def reset_dialogue(self):
        # type: () -> None
        """
        Restarts the dialogue from the start.
        """
        self.current_action = self.dialogue_root
        self.should_cancel = False
        self.is_canceled = False

    def cancel_dialogue(self, next_topic):
        # type: (DialogueTopic) -> None
        """
        Request to cancel this dialogue as soon as a DialogueLine is reached that can be canceled.
        :param next_topic: The topic this one was cancelled for. Is None when the dialogue manager is shutdown.
        """
        rospy.loginfo("Dialogue cancel requested.")

        self.should_cancel = True

import rospy
from keyboard.msg import Key
from typing import Union

from abstract_dialogue_action import AbstractDialogueAction
from abstract_dialogue_action_talk import AbstractDialogueActionTalk


class DialogueActionTalkBinaryResponse(AbstractDialogueActionTalk):
    """
    DialogueActionTalkBinaryResponse makes the Sota utter a sentence and allows the user to respond by pressing either
    the 'y' or 'n' keys on their keyboard.
    """

    def __init__(self, utterance, cancelable, next_action_yes, next_action_no):
        # type: (str, bool, Union[AbstractDialogueAction, None], Union[AbstractDialogueAction, None]) -> None
        self.utterance = utterance
        self.cancelable = cancelable
        self.next_action_yes = next_action_yes
        self.next_action_no = next_action_no

    def run(self, tf):
        # type: (str) -> AbstractDialogueAction
        """
        Use this function to perform an action and return the next action. Return None when there is no next action.
        :param tf: The name of the tf2_ros transform of the object that is currently being talked about.
        :return: The next action in the Dialogue. Return None when there is no next action.
        """
        AbstractDialogueActionTalk.utter(self.utterance)

        while True:
            key = rospy.wait_for_message('/keyboard/keydown', Key) # type: Key

            rospy.loginfo("Key {} pressed.".format(key.code))

            if key.code == Key.KEY_y:
                return self.next_action_yes
            if key.code == Key.KEY_n:
                return self.next_action_no

    def can_cancel(self):
        # type () -> bool
        """
        Whether the Dialogue can logically be cancelled after this DialogueAction.
        :return: Is this a good place in the Dialogue to stop if the Dialogue has to be cancelled?
        """
        return self.cancelable

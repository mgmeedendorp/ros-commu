from typing import Union

from abstract_dialogue_action import AbstractDialogueAction
from abstract_dialogue_action_talk import AbstractDialogueActionTalk


class DialogueActionTalkNoResponse(AbstractDialogueActionTalk):
    """
    DialogueActionTalkNoResponse makes the Sota utter a sentence, without allowing the user to respond.
    """

    def __init__(self, utterance, cancelable, next_action):
        # type: (str, bool, Union[AbstractDialogueAction, None]) -> None
        self.utterance = utterance
        self.cancelable = cancelable
        self.next_action = next_action

    def run(self, tf):
        # type: (str) -> AbstractDialogueAction
        """
        Use this function to perform an action and return the next action. Return None when there is no next action.
        :param tf: The name of the tf2_ros transform of the object that is currently being talked about.
        :return: The next action in the Dialogue. Return None when there is no next action.
        """
        AbstractDialogueActionTalk.utter(self.utterance)

        return self.next_action

    def can_cancel(self):
        # type () -> bool
        """
        Whether the Dialogue can logically be cancelled after this DialogueAction.
        :return: Is this a good place in the Dialogue to stop if the Dialogue has to be cancelled?
        """
        return self.cancelable

from user_input import *
from abstract_dialogue_line import AbstractDialogueLine


class DialogueLineAnyResponse(DialogueLineNoResponse):
    """
    Wait for the conversation partner to finish talking after asking a question.
    """

    def request_user_response(self):
        # type: () -> AbstractUserInput
        return AnyInput()
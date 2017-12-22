from user_input import *
from dialogue_line_no_response import DialogueLineNoResponse


class DialogueLineAnyResponse(DialogueLineNoResponse):
    """
    Wait for the conversation partner to finish talking after asking a question.
    """

    def request_user_response(self):
        # type: () -> AbstractUserInput
        return AnyInput()
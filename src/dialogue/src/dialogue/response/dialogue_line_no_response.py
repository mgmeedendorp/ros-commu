from user_input import *
from abstract_dialogue_line import AbstractDialogueLine


class DialogueLineNoResponse(AbstractDialogueLine):
    """
    DialogueLineNoResponse represents an utterance for which no answer is expected, and no time is given for a response.
    """

    def __init__(self, utterance, cancelable, next_line):
        # type: (str, bool, AbstractDialogueLine) -> None
        self.utterance = utterance
        self.next_line = next_line
        self.cancelable = cancelable

    def get_next_line(self, response):
        # type: (str) -> AbstractDialogueLine
        return self.next_line

    def get_utterance(self):
        # type: () -> str
        return self.utterance

    def request_user_response(self):
        # type: () -> AbstractUserInput
        return NoInput()

    def can_cancel(self):
        return self.cancelable

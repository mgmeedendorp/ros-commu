from user_input import *
from abstract_dialogue_line import AbstractDialogueLine
from dialogue_line_repeat_please import DialogueLineRepeatPlease


class DialogueLineBinaryResponse(AbstractDialogueLine):
    """
    DialogueLineBinaryResponse indicates a simple yes/no question. It uses a BinaryResponse wait for user input and
    chooses the next line based on it.
    """

    def __init__(self, utterance, cancelable, next_line_yes, next_line_no):
        # type: (str, bool, AbstractDialogueLine, AbstractDialogueLine) -> None
        self.utterance = utterance
        self.next_line_yes = next_line_yes
        self.next_line_no = next_line_no
        self.cancelable = cancelable

    def get_next_line(self, response):
        # type: (str) -> AbstractDialogueLine

        # Didn't hear yes or no, ask again..
        if response == BinarySpeechInput.NOT_RECOGNIZED:
            return DialogueLineRepeatPlease(self)

        if response == BinarySpeechInput.BINARY_YES:
            return self.next_line_yes
        return self.next_line_no

    def get_utterance(self):
        # type: () -> str
        return self.utterance

    def request_user_response(self):
        # type: () -> AbstractUserInput
        return BinarySpeechInput()

    def can_cancel(self):
        return self.cancelable

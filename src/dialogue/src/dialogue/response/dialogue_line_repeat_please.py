from user_input import *
from abstract_dialogue_line import AbstractDialogueLine


class DialogueLineRepeatPlease(AbstractDialogueLine):
    """
    Ask for the conversation partner to repeat the last answer because it was misunderstood.
    """

    def __init__(self, dialogue_line_to_copy):
        # type: (AbstractDialogueLine) -> None
        self.dialogue_line_to_copy = dialogue_line_to_copy

    def get_next_line(self, response):
        # type: (str) -> AbstractDialogueLine
        return self.dialogue_line_to_copy.get_next_line(response)

    def get_utterance(self):
        # type: () -> str
        return "I'm sorry, could you please repeat that?"

    def request_user_response(self):
        # type: () -> AbstractUserInput
        return self.dialogue_line_to_copy.request_user_response()

    def can_cancel(self):
        return self.dialogue_line_to_copy.can_cancel()
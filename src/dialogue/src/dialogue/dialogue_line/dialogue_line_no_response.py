from user_input import *
from abstract_dialogue_line import AbstractDialogueLine


class DialogueLineNoResponse(AbstractDialogueLine):
    """
    DialogueLineNoResponse represents an utterance for which no answer is expected, and no time is given for a response.
    """

    def __init__(self, utterance, cancelable, next_line, look_at_conversation_object=True, look_at_object_frame=None, look_at_object_time=0):
        # type: (str, bool, AbstractDialogueLine, bool, str, int) -> None
        self.utterance = utterance
        self.next_line = next_line
        self.cancelable = cancelable

        self.look_at_conversation_object = look_at_conversation_object
        self.look_at_object_frame = look_at_object_frame
        self.look_at_object_time = look_at_object_time

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

    def get_look_target(self, tf_talking_about):
        # type: (str) -> (str, int)
        return (tf_talking_about if self.look_at_conversation_object else self.look_at_object_frame, self.look_at_object_time)

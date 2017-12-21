from abstract_user_input import AbstractUserInput
from time import sleep


class AnyInput(AbstractUserInput):
    """
    AnySpeechInput indicates that we want the conversation partner to answer, but since there is no way to
    parse the answer of the conversation partner, we simply wait for silence. #TODO this is obsolete after stt_response
    """

    def get_response(self):
        # type: () -> str
        sleep(3)  # TODO wait for silence
        return ""
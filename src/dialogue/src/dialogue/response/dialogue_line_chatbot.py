from user_input import *
from abstract_dialogue_line import AbstractDialogueLine
from chatbot import *


class DialogueLineChatbot:
    """
    Generate a dialogue line based on the Mitsuku chatbot and request user response via pocketsphinx.
    """

    def __init__(self):
        self.mitsuku = Mitsuku()
        self.speech_input = SpeechInput("alsa_input.usb-C-Media_Electronics_Inc._USB_PnP_Sound_Device-00.analog-mono")

    def get_next_line(self, response):
        # type: (str) -> AbstractDialogueLine
        raise NotImplementedError

    def get_utterance(self):
        # type: () -> str

        if previous_response is "":
            previous_response = "Hi there!"

        return self.mitsuku.getResponse(previous_response)

    def request_user_response(self):
        # type: () -> AbstractUserInput
        return self.speech_input

    def can_cancel(self):
        # type: () -> bool
        """
        Whether the dialogue can be cancelled after uttering this line. (no cancelling after a question, for example).
        :return: Whether the dialogue can be cancelled after this line.
        """
        return True #TODO figure out if there's a better way of doing this.
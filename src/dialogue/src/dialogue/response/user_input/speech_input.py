from abstract_user_input import AbstractUserInput
from pocketsphinx import LiveSpeech


class SpeechInput(AbstractUserInput):
    """
    SpeechInput uses Pocketsphinx to do voice recognition and returns the spoken text.
    """

    def __init__(self, audio_device):
        self.livespeech = LiveSpeech(audio_device=audio_device, full_utt=True)

    def get_response(self):
        # type: () -> str

        return self.livespeech.__iter__().next()
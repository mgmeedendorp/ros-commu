from abstract_user_input import AbstractUserInput
from time import sleep
import rospy
from pocketsphinx import *


class AnyInput(AbstractUserInput):
    """
    AnySpeechInput indicates that we want the conversation partner to answer, but since there is no way to
    parse the answer of the conversation partner, we simply wait for silence.
    """

    def __init__(self):
        audio_input_device = rospy.get_param(
            'dialogue/audio_input_device',
            "alsa_input.usb-C-Media_Electronics_Inc._USB_PnP_Sound_Device-00.analog-mono"
        )

        self.livespeech = LiveSpeech(audio_device=audio_input_device)

    def get_response(self):
        # type: () -> str

        self.livespeech.__iter__().next()

        return ""
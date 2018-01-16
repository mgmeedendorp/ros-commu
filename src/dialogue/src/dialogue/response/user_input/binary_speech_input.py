from abstract_user_input import AbstractUserInput
from pocketsphinx import *
import rospy

class BinarySpeechInput(AbstractUserInput):
    """
    BinarySpeechInput is a response which the conversation partner gives by saying either yes or no.

    This could be improved by not just recognizing yes or no but performing positive/negative sentiment recognition.
    """

    def __init__(self):
        audio_input_device = rospy.get_param(
            'dialogue/audio_input_device',
            "alsa_input.usb-C-Media_Electronics_Inc._USB_PnP_Sound_Device-00.analog-mono"
        )

        self.livespeech = LiveSpeech(audio_device=audio_input_device)

    BINARY_NO = "no"
    BINARY_YES = "yes"
    NOT_RECOGNIZED = "undefined"

    def get_response(self):
        # type: () -> str
        rospy.loginfo("Waiting for user speech input...")
        rospy.loginfo("Say either 'yes' or 'no'.")

        input = self.livespeech.__iter__().next()  # type: str

        if 'yes' in input:
            return self.BINARY_YES

        if 'no' in input:
            return self.BINARY_NO

        return self.NOT_RECOGNIZED

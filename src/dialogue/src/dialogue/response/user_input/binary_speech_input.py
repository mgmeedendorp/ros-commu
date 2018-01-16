from abstract_user_input import AbstractUserInput
from pocketsphinx import *
import rospy

class BinarySpeechInput(AbstractUserInput):
    """
    BinarySpeechInput is a response which the conversation partner gives by saying either yes or no.

    This could be improved by not just recognizing yes or no but performing positive/negative sentiment recognition.
    """

    BINARY_NO = "no"
    BINARY_YES = "yes"
    NOT_RECOGNIZED = "undefined"

    def get_response(self, livespeech):
        # type: (LiveSpeech) -> str
        rospy.loginfo("Waiting for user speech input...")
        rospy.loginfo("Say either 'yes' or 'no'.")

        str_in = livespeech.__iter__().next()  # type: str

        rospy.loginfo("[BinarySpeechInput] Heard user input '{}' from speech input.".format(str_in))

        if 'yes' in str_in:
            return self.BINARY_YES

        if 'no' in str_in:
            return self.BINARY_NO

        return self.NOT_RECOGNIZED

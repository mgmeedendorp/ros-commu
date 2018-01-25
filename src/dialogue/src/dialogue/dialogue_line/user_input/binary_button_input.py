from abstract_user_input import AbstractUserInput
from pocketsphinx import *
import rospy

class BinaryButtonInput(AbstractUserInput):
    """
    BinaryButtonInput is a response which the conversation partner gives by saying either yes or no.

    This could be improved by not just recognizing yes or no but performing positive/negative sentiment recognition.
    """

    BINARY_NO = "no"
    BINARY_YES = "yes"

    def get_response(self):
        # type: () -> str

        #TODO: Make this listen to a button

        return self.BINARY_NO

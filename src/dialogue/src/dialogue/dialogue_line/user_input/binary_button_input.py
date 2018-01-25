from keyboard.msg import Key

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

        while True:
            key = rospy.wait_for_message('/keyboard/keydown', Key) # type: Key

            rospy.loginfo("Key {} pressed.".format(key.code))

            if key.code == Key.KEY_y:
                return self.BINARY_YES
            if key.code == Key.KEY_n:
                return self.BINARY_NO

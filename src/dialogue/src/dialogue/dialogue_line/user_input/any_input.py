from abstract_user_input import AbstractUserInput
from time import sleep
import rospy
from pocketsphinx import *

class AnyInput(AbstractUserInput):
    """
    AnySpeechInput indicates that we want the conversation partner to answer, but since there is no voice input, we
    simply wait for 2 seconds.
    """

    def get_response(self):
        # type: () -> str

        sleep(2)

        return ""
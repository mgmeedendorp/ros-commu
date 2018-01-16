from abstract_user_input import AbstractUserInput
from time import sleep
import rospy
from pocketsphinx import *


class AnyInput(AbstractUserInput):
    """
    AnySpeechInput indicates that we want the conversation partner to answer, but since there is no way to
    parse the answer of the conversation partner, we simply wait for silence.
    """

    def get_response(self, livespeech):
        # type: (LiveSpeech) -> str

        rospy.loginfo("Waiting for user speech input...")

        livespeech.__iter__().next()

        return ""
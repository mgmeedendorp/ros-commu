from abstract_user_input import AbstractUserInput
import rospy
from pocketsphinx import LiveSpeech


class NoInput(AbstractUserInput):
    """
    NoInput indicates that no response is expected of the conversation partner.
    """
    def get_response(self, livespeech):
        # type: (LiveSpeech) -> str

        rospy.loginfo("Continuing conversation, no user input required.")

        return ""
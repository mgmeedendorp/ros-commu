from .helper.robot.cumhelper import CUMHelper
from .debug_window import DebugWindow
import rospy

class CommUWrapper:

    def __init__(self, commu_ip = "127.0.0.1", commu_port = 6019):
        # type: (str, int, DebugWindow) -> CommUWrapper
        """
        Instantiates a new CommUWrapper instance. This wraps all the functions of the CommU Helper python library,
        found under ./helper/.
        :param commu_ip: The ip address of the CommU to control.
        :param commu_port: The port of the CUMServer on the CommU.
        """
        self.cumhelper = CUMHelper(commu_ip, commu_port)

        rospy.loginfo("CommUWrapper instance created.")

    def utter(self, utterance, blocking = False, english = True):
        # type: (str, bool, bool) -> bool
        """
        Makes the CommU utter the specified string.
        :param utterance: The string to utter.
        :param blocking: Whether to block this thread until the CommU is done uttering. Utter time is approximated,
            since the CommU does not support this natively.
        :param english: Whether to utter using the english text-to-speech engine. When english is False, utterances will
            be produced using the japanese text-to-speech engine.
        :return: Whether the CommU received the command successfully.
        """
        rospy.loginfo("Saying '%s' in %s..", utterance, ("English" if english else "Japanese"))

        if english:
            return self.cumhelper.say_eng(utterance, blocking)
        else:
            return self.cumhelper.say(utterance, blocking)
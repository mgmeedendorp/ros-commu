from .helper.robot.cumhelper import CUMHelper
from .debug_handler import DebugHandler
import rospy


class CommUWrapper:
    def __init__(self, commu_ip="127.0.0.1", commu_port=6019, debug_handler=None):
        # type: (str, int, DebugHandler) -> CommUWrapper
        """
        Instantiates a new CommUWrapper instance. This wraps all the functions of the CommU Helper python library,
        found under ./helper/.
        :param commu_ip: The ip address of the CommU to control.
        :param commu_port: The port of the CommUManager on the CommU.
        :param debug_handler: The DebugHandler to use
        """
        self.cumhelper = CUMHelper(commu_ip, commu_port)
        self.debug_handler = debug_handler

        rospy.loginfo("CommUWrapper instance created.")

    def utter(self, utterance, blocking=False, english=True):
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

    def look(self, look, resolution, translation, rotation):
        # type: (dict, dict, dict, dict) -> bool
        """
        Makes the CommU look at the specified pixel location on the camera. The camera translation and rotation relative
        to the base of the head of the CommU should be provided.
        :param look: A dict containing the x ([0, resolution.x>) and y ([0, resolution.y>) coordinates specifying where
            the CommU should look.
        :param resolution: The resolution of the camera image.
        :param translation: The translation of the camera relative to the base of the head of the robot (for now).
        :param rotation: The rotation of the camera relative to the base of the head of the robot (for now).
        :return: Whether the operation was received by the CommU successfully.
        """

        # TODO: figure out how this works on the CommU
        rospy.loginfo("Look is not implemented on the CommU yet!. Please note that this will not affect the robot!")

        return True

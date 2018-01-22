from helper.robot.cumhelper import CUMHelper
from debug_handler import DebugHandler
import rospy


class CommUWrapper:
    def __init__(self, commu_ip="127.0.0.1", commu_port=6019, commu_volume=10, debug_handler=None):
        # type: (str, int, int, DebugHandler) -> None
        """
        Instantiates a new CommUWrapper instance. This wraps all the functions of the CommU Helper python library,
        found under ./helper/.
        :param commu_ip: The ip address of the CommU to control.
        :param commu_port: The port of the CommUManager on the CommU.
        :param commu_volume: The volume of the CommU. Possible values in range [0, 100].
        :param debug_handler: The DebugHandler to use
        """
        self.cumhelper = CUMHelper(commu_ip, commu_port)
        self.cumhelper.chvolume(commu_volume)
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

        if self.debug_handler is not None:
            self.debug_handler.commu_utter_received(utterance, blocking, english)

        if english:
            return self.cumhelper.say_eng(utterance, blocking)
        else:
            return self.cumhelper.say(utterance, blocking)

    def look(self, x, y, z):
        # type: (int, int, int) -> bool
        """
        Makes the CommU look at the specified pixel location on the camera. The camera translation and rotation relative
        to the base of the head of the CommU should be provided.
        :param x: The x coordinate of the position to look at in millimeter.
            The x-axis is horizontal, increases towards left from the robot and is 0 between its eyes.
        :param y: The y coordinate of the position to look at in millimeter.
            The y-axis is vertical, increases towards the head of the robot and is 0 at the bottom of its body.
        :param z: The z coordinate of the position to look at in millimeter.
            The z-axis is horizontal, increases in front of the robot with 0 being at the center of rotation of the head yaw.
        :return: Whether the operation was received by the CommU successfully.
        """
        rospy.loginfo("Looking at position (%d, %d, %d)", x, y, z)

        if self.debug_handler is not None:
            self.debug_handler.commu_look_received(x, y, z)

        return self.cumhelper.look_manual(x, y, z)

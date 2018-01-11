import rospy
import tf2_ros
from realsense_person.msg import PersonDetection
from commu_wrapper.srv import CommULook
from util import get_srv_function
import transform_broadcaster
import math


class LookManager:
    def __init__(self, t_x, t_y, t_z, r_x, r_y, r_z):
        """
        Instantiates LookManager
        :param t_x: Translation of the camera relative to base of CommU head on x-axis in meters on the ROS coordinate system.
        :param t_y: Translation of the camera relative to base of CommU head on y-axis in meters on the ROS coordinate system.
        :param t_z: Translation of the camera relative to base of CommU head on z-axis in meters on the ROS coordinate system.
        :param r_x: Rotation of the camera relative to the CommU on the x-axis in degrees on the ROS coordinate system.
        :param r_y: Rotation of the camera relative to the CommU on the y-axis in degrees on the ROS coordinate system.
        :param r_z: Rotation of the camera relative to the CommU on the z-axis in degrees on the ROS coordinate system.
        """
        self.t_x = t_x
        self.t_y = t_y
        self.t_z = t_z
        self.r_x = math.radians(r_x)
        self.r_y = math.radians(r_y)
        self.r_z = math.radians(r_z)

        self.tfBuffer = tf2_ros.Buffer()
        self.tfListener = tf2_ros.TransformListener(self.tfBuffer)

    def person_classification_data(self, data):
        # type: (PersonDetection) -> None

        if len(data.persons) > 0:
            person = data.persons[0]

            center_of_mass_world = person.center_of_mass.world

            x = center_of_mass_world.x
            y = center_of_mass_world.y
            z = center_of_mass_world.z

            transform_broadcaster.publish_person_transform(x, y, z)

    def publish_static_transforms(self):
        transform_broadcaster.publish_commu_head_yaw_transform()
        transform_broadcaster.publish_euclid_transform(self.t_x, self.t_y, self.t_z, self.r_x, self.r_y, self.r_z)

    def request_commu_look(self):
        try:
            transform = self.tfBuffer.lookup_transform("commu_head_yaw", "person", rospy.Time(), rospy.Duration(1))  # type: geometry_msgs.msg.TransformStamped

        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
            rospy.loginfo("No transform found between commu_head_yaw and person. This can happen occasionally.")
            return

        rospy.loginfo("person transform yay")

        tx = transform.transform.translation.x
        ty = transform.transform.translation.y
        tz = transform.transform.translation.z

        x, y, z = self.convert_ros_to_commu_coords(tx, ty, tz)

        commu_look_function = get_srv_function('/commu_wrapper/look', CommULook)
        result = commu_look_function(x, y, z)

        if not result:
            rospy.logerr("Call to /commu_wrapper/look failed!")


    def convert_ros_to_commu_coords(self, xRos, yRos, zRos):
        # Swap axes and convert to millimeters.
        xCommU = yRos * 1000
        yCommU = zRos * 1000
        zCommU = xRos * 1000

        return xCommU, yCommU, zCommU

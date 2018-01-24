import random

import rospy
import tf2_ros
from geometry_msgs.msg import TransformStamped
from realsense_person.msg import PersonDetection
from commu_wrapper.srv import CommULook
from ssd.msg import ClassifiedObjectArray
from util import get_srv_function
import transform_broadcaster
import math


class LookManager:
    def __init__(self,
                 euclid_t_x, euclid_t_y, euclid_t_z,
                 euclid_r_x, euclid_r_y, euclid_r_z,
                 webcam_t_x, webcam_t_y, webcam_t_z,
                 webcam_r_x, webcam_r_y, webcam_r_z):
        """
        Instantiates LookManager
        :param euclid_t_x: Translation of the euclid relative to base of CommU head on x-axis in meters on the ROS coordinate system.
        :param euclid_t_y: Translation of the euclid relative to base of CommU head on y-axis in meters on the ROS coordinate system.
        :param euclid_t_z: Translation of the euclid relative to base of CommU head on z-axis in meters on the ROS coordinate system.
        :param euclid_r_x: Rotation of the euclid relative to the CommU on the x-axis in degrees on the ROS coordinate system.
        :param euclid_r_y: Rotation of the euclid relative to the CommU on the y-axis in degrees on the ROS coordinate system.
        :param euclid_r_z: Rotation of the euclid relative to the CommU on the z-axis in degrees on the ROS coordinate system.
        :param webcam_t_x: Translation of the webcam relative to base of CommU head on x-axis in meters on the ROS coordinate system.
        :param webcam_t_y: Translation of the webcam relative to base of CommU head on y-axis in meters on the ROS coordinate system.
        :param webcam_t_z: Translation of the webcam relative to base of CommU head on z-axis in meters on the ROS coordinate system.
        :param webcam_r_x: Rotation of the webcam relative to the CommU on the x-axis in degrees on the ROS coordinate system.
        :param webcam_r_y: Rotation of the webcam relative to the CommU on the y-axis in degrees on the ROS coordinate system.
        :param webcam_r_z: Rotation of the webcam relative to the CommU on the z-axis in degrees on the ROS coordinate system.
        """
        self.euclid_t_x = euclid_t_x
        self.euclid_t_y = euclid_t_y
        self.euclid_t_z = euclid_t_z
        self.euclid_r_x = math.radians(euclid_r_x)
        self.euclid_r_y = math.radians(euclid_r_y)
        self.euclid_r_z = math.radians(euclid_r_z)

        self.webcam_t_x = webcam_t_x
        self.webcam_t_y = webcam_t_y
        self.webcam_t_z = webcam_t_z
        self.webcam_r_x = math.radians(webcam_r_x)
        self.webcam_r_y = math.radians(webcam_r_y)
        self.webcam_r_z = math.radians(webcam_r_z)

        self.latest_classified_object_data = None  # type: ClassifiedObjectArray

        self.tfBuffer = tf2_ros.Buffer()
        self.tfListener = tf2_ros.TransformListener(self.tfBuffer)

        self.target_frame_name = None  # type: str

    def set_look_at_target(self, frame_name):
        # type: (str) -> bool
        self.target_frame_name = frame_name

        return True

    def person_classification_data(self, data):
        # type: (PersonDetection) -> None

        if len(data.persons) > 0:
            person = data.persons[0]

            center_of_mass_world = person.center_of_mass.world

            x = center_of_mass_world.x
            y = center_of_mass_world.y
            z = center_of_mass_world.z

            transform_broadcaster.publish_person_transform(x, y, z)

    def classified_object_data(self, data):
        # type: (ClassifiedObjectArray) -> None

        self.latest_classified_object_data = data

    def publish_static_transforms(self):
        transform_broadcaster.publish_commu_head_yaw_transform()
        transform_broadcaster.publish_euclid_transform(
            self.euclid_t_x, self.euclid_t_y, self.euclid_t_z,
            self.euclid_r_x, self.euclid_r_y, self.euclid_r_z
        )
        transform_broadcaster.publish_webcam_transform(
            self.webcam_t_x, self.webcam_t_y, self.webcam_t_z,
            self.webcam_r_x, self.webcam_r_y, self.webcam_r_z
        )

    def request_commu_look(self):
        if self.target_frame_name is not None:
            try:
                transform = self.tfBuffer.lookup_transform("commu_head_yaw", self.target_frame_name, rospy.Time(), rospy.Duration(1))  # type: geometry_msgs.msg.TransformStamped

            except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
                rospy.loginfo("No transform found between commu_head_yaw and {}. This can happen occasionally.".format(self.target_frame_name))
                return

            tx = transform.transform.translation.x
            ty = transform.transform.translation.y
            tz = transform.transform.translation.z
        else:
            # Look around somewhere
            tx = 0.5 - random.random()
            ty = 0.5 - random.random()
            tz = 0.5 - random.random()

        x, y, z = self.convert_ros_to_commu_coords(tx, ty, tz)

        commu_look_function = get_srv_function('/commu_wrapper/look', CommULook)
        success = commu_look_function(x, y, z)

        if not success:
            rospy.logerr("Call to /commu_wrapper/look failed!")

    def publish_classified_objects(self):
        if self.latest_classified_object_data is not None:
            data = self.latest_classified_object_data

            transform_broadcaster.publish_object_transform(data.camera_info, data.objects)


    def convert_ros_to_commu_coords(self, xRos, yRos, zRos):
        # Swap axes and convert to millimeters.
        xCommU = yRos * 1000
        yCommU = zRos * 1000
        zCommU = xRos * 1000

        return xCommU, yCommU, zCommU

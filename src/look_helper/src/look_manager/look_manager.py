import rospy
from realsense_person.msg import PersonDetection
from commu_wrapper.srv import CommULook
from util import get_srv_function
from transform_broadcaster import publish_euclid_transform, publish_commu_head_yaw_transform
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

    def person_classification_data(self, data):
        # type: (PersonDetection) -> None

        if len(data.persons) > 0:
            person = data.persons[0]

            center_of_mass_world = person.center_of_mass.world

            x = center_of_mass_world.x
            y = center_of_mass_world.y
            z = center_of_mass_world.z

            x = -x  # Invert x axis
            y = -y  # Invert y axis

            x *= 1000  # m to mm
            y *= 1000  # m to mm
            z *= 1000  # m to mm

            x, y, z = self.rotate(x, y, z)

            x += self.t_x
            y += self.t_y
            z += self.t_z

            x = int(x)
            y = int(y)
            z = int(z)

            commu_look_function = get_srv_function('/commu_wrapper/look', CommULook)

            result = commu_look_function(x, y, z)

    def publish_transforms(self):
        publish_commu_head_yaw_transform()
        publish_euclid_transform(self.t_x, self.t_y, self.t_z, self.r_x, self.r_y, self.r_z)



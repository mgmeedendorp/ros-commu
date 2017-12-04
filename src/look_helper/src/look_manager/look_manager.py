import rospy
from realsense_person.msg import PersonDetection
from commu_wrapper.srv import CommULook
from util import get_srv_function
import math


class LookManager:
    def __init__(self, t_x, t_y, t_z, r_x, r_y, r_z):
        """
        Instantiates LookManager
        :param t_x: Translation of the camera relative to neck rotation point of CommU head on x-axis in millimeters.
        :param t_y: Translation of the camera relative to neck rotation point of CommU head on y-axis in millimeters.
        :param t_z: Translation of the camera relative to neck rotation point of CommU head on z-axis in millimeters.
        :param r_x: Rotation of the camera relative to the CommU's body on the x-axis in degrees.
        :param r_y: Rotation of the camera relative to the CommU's body on the y-axis in degrees.
        :param r_z: Rotation of the camera relative to the CommU's body on the z-axis in degrees.
        """
        self.t_x = t_x
        self.t_y = t_y
        self.t_z = t_z
        self.r_x = math.radians(r_x)
        self.r_y = math.radians(r_y)
        self.r_z = math.radians(r_z)

    def person_classification_data(self, data):
        # type: (PersonDetection) -> None

        if (len(data.persons) > 0):
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

    def rotate(self, x, y, z):
        cos_x = math.cos(self.r_x)
        sin_x = math.sin(self.r_x)
        cos_y = math.cos(self.r_y)
        sin_y = math.sin(self.r_y)
        cos_z = math.cos(self.r_z)
        sin_z = math.sin(self.r_z)

        # Rotation around z
        x = x * cos_z - y * sin_z
        y = x * sin_z + y * cos_z

        # Rotation around y
        x = x * cos_y + z * sin_y
        z = -x * sin_y + z * cos_y

        # Rotation around x
        y = y * cos_x - z * sin_x
        z = y * sin_x + z * cos_x

        return x, y, z

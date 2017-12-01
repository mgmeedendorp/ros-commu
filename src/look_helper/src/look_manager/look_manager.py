import rospy
from realsense_person.msg import PersonDetection
from commu_wrapper.srv import CommULook
from util import get_srv_function

class LookManager:
    commu_look_function = get_srv_function('/commu_wrapper/look', CommULook)

    def person_classification_data(self, data):
        # type: (PersonDetection) -> None

        person = data.persons[0]

        center_of_mass_world = person.center_of_mass.world


        x = center_of_mass_world.x * 1000 #m to mm
        y = center_of_mass_world.y * 1000 #m to mm
        z = center_of_mass_world.z * 1000 #m to mm

        result = LookManager.commu_look_function(x, y, z)

        rospy.loginfo("looking at (%d, %d, %d), result: " + result, x, y, z) #TODO remove this
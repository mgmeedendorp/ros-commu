import rospy
from realsense_person.msg import PersonDetection
from commu_wrapper.srv import CommULook
from util import get_srv_function

class LookManager:

    def person_classification_data(self, data):
        # type: (PersonDetection) -> None

        if(len(data.persons) > 0):
            person = data.persons[0]

            center_of_mass_world = person.center_of_mass.world

            x = int(center_of_mass_world.x * 1000) #m to mm
            y = int(center_of_mass_world.y * 1000) #m to mm
            z = int(center_of_mass_world.z * 1000) #m to mm

            x = -x # Invert x axis

            y += 200 #Camera is not on ground

            commu_look_function = get_srv_function('/commu_wrapper/look', CommULook)

            result = commu_look_function(x, y, z)

            rospy.loginfo("looking at (%d, %d, %d), result: " + str(result.success), x, y, z) #TODO remove this
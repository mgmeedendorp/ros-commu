from realsense_person.msg import PersonDetection

class LookManager:


    def person_classification_data(self, data):
        # type: (PersonDetection) -> None

        person = data.persons[0]

        center_of_mass = person.center_of_mass

        x = center_of_mass.x * 1000 #m to mm
        y = center_of_mass.y * 1000 #m to mm
        z = center_of_mass.z * 1000 #m to mm


#!/usr/bin/env python

import rospy
from look_manager import *
from realsense_person.msg import PersonDetection

def person_classification_callback(manager, data):
    manager.person_classification_data(data)


def init_message_listeners(manager):
    # type: (LookManager) -> None
    def person_callback(data):
        # type: (PersonDetection) -> None
        person_classification_callback(manager, data)
        print "Person classification received stdout"
        rospy.loginfo("Person classification received.")

    rospy.Subscriber("/camera/person/detection_data", PersonDetection, person_callback)


def init_message_publishers(manager):
    pass


if __name__ == '__main__':
    rospy.init_node("look_helper")
    rospy.loginfo("Starting look_helper node..")

    rospy.loginfo("Creating LookManager..")
    manager = LookManager()

    init_message_listeners(manager)
    init_message_publishers(manager)

    #manager.start(utter, threaded=True, perpetual=True)

    rospy.spin()
#!/usr/bin/env python

import rospy
from look_manager import *
from realsense_person.msg import PersonDetection
import time


last_classification_time = 0


def person_classification_callback(manager, data):
    # type: (LookManager, PersonDetection) -> None
    global last_classification_time

    rospy.loginfo("Person classification received.")

    if(time.time() - last_classification_time >= 1):
        manager.person_classification_data(data)
        last_classification_time = time.time()


def init_message_listeners(manager):
    # type: (LookManager) -> None
    def person_callback(data):
        # type: (PersonDetection) -> None
        person_classification_callback(manager, data)

    rospy.Subscriber("/camera/person/detection_data", PersonDetection, person_callback)


def init_message_publishers(manager):
    pass


if __name__ == '__main__':
    rospy.init_node("look_helper")
    rospy.loginfo("Starting look_helper node..")

    rospy.loginfo("Creating LookManager..")
    manager = LookManager(0, 0, 30, 45, 0, 0)

    init_message_listeners(manager)
    init_message_publishers(manager)

    #manager.start(utter, threaded=True, perpetual=True)

    rospy.spin()
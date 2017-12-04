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

    t_x = rospy.get_param('tx', 0)
    t_y = rospy.get_param('ty', 0)
    t_z = rospy.get_param('tz', 0)

    r_x = rospy.get_param('rx', 0)
    r_y = rospy.get_param('ry', 0)
    r_z = rospy.get_param('rz', 0)

    rospy.loginfo("LookManager initializing with: {tx: %f, ty: %f, tz: %f, rx: %f, ry: %f, rx: %f}", t_x, t_y, t_z, r_x, r_y, r_z)

    manager = LookManager(t_x, t_y, t_z, r_x, r_y, r_z)

    init_message_listeners(manager)
    init_message_publishers(manager)

    rospy.spin()
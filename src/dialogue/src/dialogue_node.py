#!/usr/bin/env python

import rospy
from ssd.msg import ClassifiedObjectArray
from commu_wrapper.srv import CommUUtter
from dialogue import *
from util import get_srv_function

def classification_result_callback(manager, data):
    priority = 0.5

    if data.label == "person":
        priority = 1.0

    manager.add_topic(data.label, priority)


def init_message_listeners(manager):
    def callback(data):
        classification_result_callback(manager, data)

    rospy.Subscriber("/ssd_node/classification_result", ClassifiedObjectArray, callback)


def init_message_publishers(manager):
    pass


def utter(utterance):
    utter_srv = get_srv_function('/commu_wrapper/utter', CommUUtter)

    rospy.loginfo("Uttering: " + utterance)

    success = utter_srv(utterance, True, True)

    rospy.loginfo("Uttering " + ("succeeded" if success else "failed!"))

    return success


if __name__ == '__main__':
    rospy.init_node("dialogue")
    rospy.loginfo("Starting dialogue node..")

    rospy.loginfo("Creating DialogueManager..")
    manager = DialogueManager(CommUDialogueLibrary())

    init_message_listeners(manager)
    init_message_publishers(manager)

    manager.start(utter, threaded=True, perpetual=True)

    rospy.spin()
#!/usr/bin/env python

import rospy
from ssd.msg import ClassifiedObjectArray
from commu_wrapper.srv import CommUUtter
from dialogue import *
from util import get_srv_function


def classification_result_callback(manager, data):
    rospy.logdebug("Received classification results with {} objects.".format(len(data.objects)))

    for obj in data.objects:
        short_term_history = manager.get_topic_history()[-10:]

        count = short_term_history.count(obj.label)

        if count <= 0:
            if obj.label == "person":
                manager.add_topic(obj.label, 1)
            else:
                manager.add_topic(obj.label, .9)


def init_message_listeners(manager):
    rospy.loginfo("Initializing message listeners...")

    def classification_callback(data):
        classification_result_callback(manager, data)

    rospy.Subscriber("/ssd_node/classification_result", ClassifiedObjectArray, classification_callback)

    rospy.loginfo("Initializing message listeners done.")


def init_message_publishers(manager):
    rospy.loginfo("Initializing message publishers...")

    rospy.loginfo("Initializing message publishers done.")


def utter(utterance):
    utter_srv = get_srv_function('/commu_wrapper/utter', CommUUtter)

    rospy.loginfo("Uttering: " + str(utterance))

    if utterance is not None:
        success = utter_srv(utterance, True, True)

        rospy.loginfo("Uttering " + ("succeeded" if success else "failed!"))

        return success
    return True


if __name__ == '__main__':
    rospy.init_node("dialogue")
    rospy.loginfo("Starting dialogue node..")

    rospy.loginfo("Creating DialogueManager..")

    manager = DialogueManager(CommUDialogueLibrary())

    rospy.loginfo("DialogueManager created.")

    init_message_listeners(manager)
    init_message_publishers(manager)

    manager.start(utter, True)

    rospy.loginfo("Dialogue node started.")
    try:
        rospy.spin()
    finally:
        manager.stop(force=True)

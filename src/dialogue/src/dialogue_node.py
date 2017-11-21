#!/usr/bin/env python

import rospy
from ssd.msg import ClassifiedObjectArray
from realsense_person.msg import PersonDetection
from commu_wrapper.srv import CommUUtter
from dialogue import *
from util import get_srv_function


def classification_result_callback(manager, data):
    rospy.logdebug("Received classification results with {} objects.".format(len(data.objects)))

    for obj in data.objects:
        priority = 0.5

        short_term_history = manager.get_topic_history()[-10:]

        count = short_term_history.count(obj.label)

        if count > 0:
            priority -= 0.3 * count

        if priority > 0:
            manager.add_topic(obj.label, priority)

def person_classification_callback(manager, data):
    rospy.loginfo("Person classification data: " + data)


def init_message_listeners(manager):
    def classification_callback(data):
        classification_result_callback(manager, data)

    def person_callback(data):
        person_classification_callback(manager, data)

    rospy.Subscriber("/ssd_node/classification_result", ClassifiedObjectArray, classification_callback)
    rospy.Subscriber("/camera/person/classification_data", PersonDetection, person_callback)


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

    try:
        rospy.spin()
    except KeyboardInterrupt:
        manager.stop(force=True)

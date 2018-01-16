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
            manager.add_topic(obj.label, 1)


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

    rospy.loginfo("Uttering: " + utterance)

    success = utter_srv(utterance, True, True)

    rospy.loginfo("Uttering " + ("succeeded" if success else "failed!"))

    return success


if __name__ == '__main__':
    rospy.init_node("dialogue")
    rospy.loginfo("Starting dialogue node..")

    rospy.loginfo("Creating DialogueManager..")

    audio_input_device = rospy.get_param(
        'dialogue/audio_input_device',
        "alsa_input.usb-C-Media_Electronics_Inc._USB_PnP_Sound_Device-00.analog-mono"
    )

    manager = DialogueManager(
        audio_input_device,
        CommUDialogueLibrary(),
        MitsukuDialogue(audio_input_device)
    )
    rospy.loginfo("DialogueManager created.")

    init_message_listeners(manager)
    init_message_publishers(manager)

    manager.start(utter, True)

    rospy.loginfo("Dialogue node started.")
    try:
        rospy.spin()
    except:
        manager.stop(force=True)

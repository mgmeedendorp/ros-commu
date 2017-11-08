#!/usr/bin/env python
import random

import rospy
import time
import argparse

import sys

from helper.robot.cumhelper import CUMHelper
from ssd.msg import ClassifiedObjectArray

from dialogue.dialogue_definitions import get_dialogue_for_label

latest_objects = None

current_dialogue = None


def callback(data):
    global latest_objects
    latest_objects = data.objects


def listener(manager):
    global current_dialogue

    rospy.init_node('commu_helper')

    rospy.Subscriber("/ssd_node/classification_result", ClassifiedObjectArray, callback)

    while not rospy.is_shutdown():
        if latest_objects is not None:
            if current_dialogue is None or not current_dialogue.dialogue_remaining():
                if len(latest_objects) != 0:
                    latest = latest_objects

                    random_object = random.choice(latest)
                    label = random_object.label

                    current_dialogue = get_dialogue_for_label(label)
            else:
                current_dialogue.proceed_dialogue(utter(manager))


def utter(manager):
    #type: (CUMHelper) -> Callable[str, None]
    def say_sync(utterance):
        # type: (str) -> None
        print("Saying: " + utterance)
        manager.say_eng(utterance, blocking=True)

    return say_sync


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="utility for CommUManager")
    parser.add_argument("-i", "--ipaddress", default="127.0.0.1")
    parser.add_argument("-p", "--port", required=True)
    parser.add_argument("-g", "--gesture", default="nod1")
    parser.add_argument("-l", "--look", default="center")
    args = parser.parse_args()

    manager = CUMHelper(args.ipaddress, int(args.port))
    manager.say_eng("Hello, I am CommU.")

    listener(manager)

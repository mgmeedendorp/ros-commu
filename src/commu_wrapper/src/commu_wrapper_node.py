#!/usr/bin/env python

import argparse

import rospy
import sys

from debug_handler import DebugHandler
from wrapper import CommUWrapper
from commu_wrapper.srv import CommUUtter, CommUUtterResponse, CommUUtterRequest, CommULook, CommULookResponse, CommULookRequest


def utter_callback(wrapper):
    def utter(req):
        # type: (CommUUtterRequest) -> CommUUtterResponse
        success = wrapper.utter(req.utterance, req.blocking, req.english)

        return CommUUtterResponse(success)

    return utter

def look_callback(wrapper):
    def look(req):
        # type: (CommULookRequest) -> CommULookResponse

        success = wrapper.look(req.look_x, req.look_y, req.look_z)

        return CommULookResponse(success)

    return look

def init_message_listeners(wrapper):
    rospy.loginfo("Initializing CommU wrapper node message listener.")

    rospy.Service('/commu_wrapper/utter', CommUUtter, utter_callback(wrapper))
    rospy.Service('/commu_wrapper/look', CommULook, look_callback(wrapper))


if __name__ == '__main__':
    rospy.init_node("commu_wrapper")

    parser = argparse.ArgumentParser(description="utility for CommUManager")
    parser.add_argument("-i", "--ipaddress", default="127.0.0.1")
    parser.add_argument("-p", "--port", default="6019")
    parser.add_argument("-d", "--debug", default="False")
    parser.add_argument("-m", "--image", default="/ssd_node/classification_result")
    parser.add_argument("-c", "--isclassificationtopic", default=True)
    parser.add_argument("-v", "--volume", default=10)
    args = parser.parse_args(rospy.myargv(sys.argv[1:]))

    rospy.loginfo("Starting commu_wrapper_node..")
    rospy.loginfo("Arguments:")
    rospy.loginfo("-i, --ipaddress: \t%s", args.ipaddress)
    rospy.loginfo("-p, --port: \t%s", args.port)
    rospy.loginfo("-d, --debug: \t%s", args.debug)
    rospy.loginfo("-m, --image: \t%s", args.image)
    rospy.loginfo("-c, --isclassificationtopic: \t%s", args.isclassificationtopic)
    rospy.loginfo("-v, --volume: \t%s", args.volume)

    if bool(args.debug):
        wrapper = CommUWrapper(args.ipaddress, int(args.port), int(args.volume), DebugHandler(args.image, bool(args.isclassificationtopic)))
    else:
        wrapper = CommUWrapper(args.ipaddress, int(args.port), int(args.volume))

    init_message_listeners(wrapper)

    rospy.spin()
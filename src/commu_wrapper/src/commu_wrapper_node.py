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

def init_service_handlers(wrapper):
    rospy.loginfo("Initializing CommU wrapper node message listener.")

    rospy.Service('/commu_wrapper/utter', CommUUtter, utter_callback(wrapper))
    rospy.Service('/commu_wrapper/look', CommULook, look_callback(wrapper))


if __name__ == '__main__':
    rospy.init_node("commu_wrapper")

    commu_ip = rospy.get_param("commu_wrapper/commu_ip", "127.0.0.1")
    commu_port = rospy.get_param("commu_wrapper/commu_port", "6009")
    commu_volume = rospy.get_param("commu_wrapper/commu_volume", 10)
    debug_mode = rospy.get_param("commu_wrapper/debug_mode", True)
    classification_topic = rospy.get_param("commu_wrapper/classification_topic", "/ssd_node/classification_result")

    rospy.loginfo("Starting commu_wrapper_node..")
    rospy.loginfo(
        """commu_wrapper initializing with: {
            commu_ip: %s,
            commu_port: %d,
            commu_volume: %f,
            debug_mode: %d,
            classification_topic: %s    
        }""", commu_ip, commu_port, commu_volume, debug_mode, classification_topic
    )


    if bool(debug_mode):
        wrapper = CommUWrapper(commu_ip, commu_port, commu_volume, DebugHandler(classification_topic))
    else:
        wrapper = CommUWrapper(commu_ip, commu_port, commu_volume)

    init_service_handlers(wrapper)

    rospy.spin()
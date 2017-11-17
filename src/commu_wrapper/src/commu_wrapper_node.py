#!/usr/bin/env python

import argparse

import rospy
from debug_handler import DebugHandler
from wrapper import CommUWrapper
from commu_wrapper.srv import CommUUtter, CommUUtterResponse, CommULook, CommULookResponse


def utter_callback(wrapper):
    def utter(req):
        success = wrapper.utter(req.utterance, req.blocking, req.english)

        return CommUUtterResponse(success)

    return utter

def look_callback(wrapper):
    def look(req):
        look = {'x': req.look_x, 'y': req.look_y}
        resolution = {'x': req.camera_info.width, 'y': req.camera_info.height}
        translation = {'x': req.camera_transform.translation.x,
                       'y': req.camera_transform.translation.y,
                       'z': req.camera_transform.translation.z}
        rotation = {'x': req.camera_transform.rotation.x,
                    'y': req.camera_transform.rotation.y,
                    'z': req.camera_transform.rotation.z,
                    'w': req.camera_transform.rotation.w}

        success = wrapper.look(look, resolution, translation, rotation)

        return CommULookResponse(success)


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


    rospy.logerr(rospy.myargv())
    args = parser.parse_args(rospy.myargv())

    rospy.loginfo("Starting commu_wrapper_node..")
    rospy.loginfo("Arguments:")
    rospy.loginfo("-i, --ipaddress: \t%s", args.ipaddress)
    rospy.loginfo("-p, --port: \t%s", args.port)
    rospy.loginfo("-d, --debug: \t%s", args.debug)
    rospy.loginfo("-m, --image: \t%s", args.image)
    rospy.loginfo("-c, --isclassificationtopic: \t%s", args.isclassificationtopic)

    if bool(args.debug):
        wrapper = CommUWrapper(args.ipaddress, int(args.port), DebugHandler(args.image, bool(args.isclassificationtopic)))
    else:
        wrapper = CommUWrapper(args.ipaddress, int(args.port))

    init_message_listeners(wrapper)

    rospy.spin()
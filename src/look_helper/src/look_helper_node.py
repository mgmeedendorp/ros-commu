#!/usr/bin/env python

import rospy
from look_helper.srv import SetLookAtTarget, SetLookAtTargetResponse, SetLookAtTargetRequest
from realsense_person.msg import PersonDetection
from ssd.msg import ClassifiedObjectArray

from look_manager import *


def person_classification_callback(manager, data):
    # type: (LookManager, PersonDetection) -> None
    manager.person_classification_data(data)

def classified_object_callback(manager, data):
    # type: (LookManager, ClassifiedObjectArray) -> None
    manager.classified_object_data(data)

def init_message_listeners(manager):
    # type: (LookManager) -> None

    rospy.loginfo("Initializing look_helper node message subscriptions.")

    def person_callback(data):
        # type: (PersonDetection) -> None
        person_classification_callback(manager, data)

    rospy.Subscriber("/camera/person/detection_data", PersonDetection, person_callback)

    def object_callback(data):
        # type: (ClassifiedObjectArray) -> None
        classified_object_callback(manager, data)
        rospy.logdebug("Received classification results with {} objects.".format(len(data.objects)))

    rospy.Subscriber("/ssd_node/classification_result", ClassifiedObjectArray, object_callback)


def init_message_publishers(manager):
    # type: (LookManager) -> None
    pass

def set_at_look_target_callback(manager, req):
    # type: (LookManager, SetLookAtTargetRequest) -> bool

    rospy.loginfo("Received service call to change look_target to '{}'.".format(req.target_frame_name))

    return manager.set_look_at_target(req.target_frame_name)

def init_service_handlers(manager):
    # type: (LookManager) -> None
    rospy.loginfo("Initializing look_helper node service handlers.")

    def set_at_look_target(req):
        # type: (SetLookAtTargetRequest) -> SetLookAtTargetResponse

        success = set_at_look_target_callback(manager, req)

        return SetLookAtTargetResponse(success)

    rospy.Service('/look_helper/look_target', SetLookAtTarget, set_at_look_target)



if __name__ == '__main__':
    rospy.init_node("look_helper")
    rospy.loginfo("Starting look_helper node..")

    rospy.loginfo("Creating LookManager..")

    euclid_t_x = rospy.get_param('look_helper/euclid_tx', 0)
    euclid_t_y = rospy.get_param('look_helper/euclid_ty', 0)
    euclid_t_z = rospy.get_param('look_helper/euclid_tz', 0)

    euclid_r_x = rospy.get_param('look_helper/euclid_rx', 0)
    euclid_r_y = rospy.get_param('look_helper/euclid_ry', 0)
    euclid_r_z = rospy.get_param('look_helper/euclid_rz', 0)
    
    webcam_t_x = rospy.get_param('look_helper/webcam_tx', 0)
    webcam_t_y = rospy.get_param('look_helper/webcam_ty', 0)
    webcam_t_z = rospy.get_param('look_helper/webcam_tz', 0)

    webcam_r_x = rospy.get_param('look_helper/webcam_rx', 0)
    webcam_r_y = rospy.get_param('look_helper/webcam_ry', 0)
    webcam_r_z = rospy.get_param('look_helper/webcam_rz', 0)

    rospy.loginfo("""LookManager initializing with: {
    euclid_tx: %f, euclid_ty: %f, euclid_tz: %f, \n 
    euclid_rx: %f, euclid_ry: %f, euclid_rx: %f, \n
    webcam_tx: %f, webcam_ty: %f, webcam_tz: %f, \n
    webcam_rx: %f, webcam_ry: %f, webcam_rx: %f, \n
    }""", 
    euclid_t_x, euclid_t_y, euclid_t_z, euclid_r_x, euclid_r_y, euclid_r_z,
    webcam_t_x, webcam_t_y, webcam_t_z, webcam_r_x, webcam_r_y, webcam_r_z)

    manager = LookManager(
        euclid_t_x, euclid_t_y, euclid_t_z, euclid_r_x, euclid_r_y, euclid_r_z,
        webcam_t_x, webcam_t_y, webcam_t_z, webcam_r_x, webcam_r_y, webcam_r_z
    )

    init_message_listeners(manager)
    init_message_publishers(manager)
    init_service_handlers(manager)

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        manager.publish_static_transforms()
        manager.publish_classified_objects()
        manager.request_commu_look()

        rate.sleep()

    rospy.loginfo("Shutting down look_helper node..")
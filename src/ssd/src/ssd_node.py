#!/usr/bin/env python
import cv2

import rospy
import time

import sys

import skimage
from sensor_msgs.msg import Image
from geometry_msgs.msg import Pose2D
from ssd.msg import ClassifiedObjectArray, ClassifiedObject, BoundingBox
import numpy as np
from skimage import img_as_ubyte
import skimage.io

import caffe
from ssd_wrapper import SSD, ClassificationResult
from util import image_to_opencv, draw_bounding_boxes, display_opencv_image, save_opencv_image
from cv_bridge import CvBridge, CvBridgeError


ssd = SSD(use_gpu=False)

latest_image_data = None
bridge = CvBridge()

publisher = None


def publisher():
    global publisher
    publisher = rospy.Publisher('ssd_node/classification_result', ClassifiedObjectArray, queue_size=5)

def callback(data):
    global latest_image_data
    latest_image_data = data


def listener():
    rospy.Subscriber("/cv_camera/image_raw", Image, callback)

    while not rospy.is_shutdown():
        if (latest_image_data != None):
            cv_image = bridge.imgmsg_to_cv2(latest_image_data, "bgr8")

            objects = ssd.classify_image(cv_image)

            msg = ClassifiedObjectArray()
            msg.objects = []
            msg.image = latest_image_data

            for obj in objects:
                msg.objects.append(obj.to_msg())

            publisher.publish(msg)

            #save_opencv_image(cv_image, '/home/maurice/catkin_ws/src/ssd/src/raw.png')

            #image_boxed = draw_bounding_boxes(cv_image, objects)
            #display_opencv_image(image_boxed)

            #save_opencv_image(cv_image, '/home/maurice/catkin_ws/src/ssd/src/boxed{}.png'.format(image_number))
            #image_number += 1




if __name__ == '__main__':
    rospy.init_node('ssd_classifier')
    publisher()
    listener()
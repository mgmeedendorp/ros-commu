from threading import Thread

import cv2
import numpy as np
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
import rospy

class DebugHandler:

    def __init__(self, camera_topic, window_name="Debug window"):
        rospy.loginfo("Initializing DebugHandler..")
        self.window_name = window_name
        self.image_bridge = CvBridge()

        self.latest_cv_image = None
        self.thread = None

        rospy.loginfo("Subscribing to '%s' topic for images..", camera_topic)
        rospy.Subscriber(camera_topic, Image, self.image_received)

        self.spin_image_window()

    def image_received(self, data):
        self.latest_cv_image = self.image_bridge.imgmsg_to_cv2(data, "bgr8")

    def spin_image_window(self):
        rospy.loginfo("Starting window image thread...")

        if self.thread is not None:
            rospy.loginfo("Someone tried to start two image windows of the same instance. This is not supposed to happen.")
            return

        def worker():
            rospy.loginfo("Initializing DebugHandler cv2 window with name: '%s'..", self.window_name)
            cv2.namedWindow(self.window_name, cv2.WINDOW_NORMAL)

            rospy.loginfo("Starting image worker thread.")

            while not rospy.is_shutdown():
                if self.latest_cv_image is not None:
                    cv2.imshow(self.window_name, self.latest_cv_image)

                cv2.waitKey(1000 / 30)

            cv2.destroyWindow(self.window_name)
            rospy.loginfo("Stopping image worker thread.")

        self.thread = Thread(target=worker)
        self.thread.start()




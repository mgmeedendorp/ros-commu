from threading import Thread

import cv2
import numpy as np
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
import rospy

class DebugHandler:

    def __init__(self, camera_topic, window_name="Debug window (press ESC to close)"):
        self.window_name = window_name
        self.image_bridge = CvBridge()

        self.latest_cv_image = None
        self.thread = None

        cv2.namedWindow(self.window_name, cv2.WINDOW_NORMAL)

        rospy.Subscriber(camera_topic, Image, self.image_received)

    def image_received(self, data):
        self.latest_cv_image = self.image_bridge.imgmsg_to_cv2(data, "bgr8")

    def spin_image_window(self):
        if self.thread is not None:
            rospy.loginfo("Someone tried to start two image windows of the same instance. This is not supposed to happen.")
            return

        def worker():
            while True:
                if self.latest_cv_image is not None:
                    if cv2.getWindowProperty('window-name', 0) < 0:
                        break

                    cv2.imshow(self.window_name, self.latest_cv_image)

                if cv2.waitKey(1/60) & 0xFF == 27:
                    break

        self.thread = Thread(target=worker)
        self.thread.start()

    def close_window(self):
        cv2.destroyWindow(self.window_name)




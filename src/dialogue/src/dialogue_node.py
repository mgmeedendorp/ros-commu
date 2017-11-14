import rospy
from ssd.msg import ClassifiedObjectArray
from dialogue import *


def classification_result_callback(data):
    pass


def init_message_listeners():
    rospy.Subscriber("/ssd_node/classification_result", ClassifiedObjectArray, classification_result_callback)

def init_message_publishers():
    pass


if __name__ == '__main__':
    rospy.init_node("dialogue")
    rospy.loginfo("Starting dialogue node..")

    init_message_listeners()
    init_message_publishers()

    rospy.spin()
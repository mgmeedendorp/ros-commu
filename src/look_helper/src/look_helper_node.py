import rospy
from look_manager import *

def init_message_listeners(manager):
    pass


def init_message_publishers(manager):
    pass


if __name__ == '__main__':
    rospy.init_node("look_helper")
    rospy.loginfo("Starting look_helper node..")

    rospy.loginfo("Creating LookManager..")
    manager = LookManager()

    init_message_listeners(manager)
    init_message_publishers(manager)

    #manager.start(utter, threaded=True, perpetual=True)

    try:
        rospy.spin()
    except KeyboardInterrupt:
        pass

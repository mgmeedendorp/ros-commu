import argparse

import rospy
from .wrapper import CommUWrapper
from commu_wrapper.srv import CommUUtter, CommUUtterResponse


def utter_callback(wrapper):
    def utter(req):
        success = wrapper.utter(req.utterance, req.blocking, req.english)

        return CommUUtterResponse(success)

    return utter


def init_message_listener(wrapper):
    rospy.loginfo("Initializing CommU wrapper node message listener.")

    rospy.Subscriber('/commu_wrapper/utter', CommUUtter, utter_callback(wrapper))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="utility for CommUManager")
    parser.add_argument("-i", "--ipaddress", default="127.0.0.1")
    parser.add_argument("-p", "--port", default="6019")
    args = parser.parse_args()

    wrapper = CommUWrapper(args.ipaddress, int(args.port))

    rospy.init_node("commu_wrapper")

    init_message_listener(wrapper)

    rospy.spin()
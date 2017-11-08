#!/usr/bin/env python
from button_input.srv import BinaryButtonInput, BinaryButtonInputResponse
import rospy


def handle_binary_button_input(req):
    print "Waiting for button input..."

    str_input = ""

    while str_input != "yes" and str_input != "no":
        str_input = raw_input("Please enter 'yes' or 'no': ")
        print "You entered", str_input

    print "Sending response.."

    return BinaryButtonInputResponse(1 if str_input == "yes" else 0)

def binary_button_input_server():
    rospy.init_node('binary_button_input')
    rospy.Service('binary_button_input', BinaryButtonInput, handle_binary_button_input)
    print "Ready to receive button input"
    rospy.spin()

if __name__ == "__main__":
    binary_button_input_server()
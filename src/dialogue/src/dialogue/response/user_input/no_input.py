from abstract_user_input import AbstractUserInput


class NoInput(AbstractUserInput):
    """
    NoInput indicates that no response is expected of the conversation partner.
    """
    def get_response(self):
        # type: () -> str

        rospy.loginfo("Continuing conversation, no user input required.")

        return ""
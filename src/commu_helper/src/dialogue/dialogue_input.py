import time
import rospy
from button_input.srv import BinaryButtonInput
from util import get_srv_function


class AbstractDialogueResponse:
    """
    AbstractDialogueResponse is an abstract class that can request a response from conversation partner
    via the get_response function.
    """

    def get_response(self):
        # type: () -> None
        """
        Blocks the thread until the conversation partner gives a response and returns that response.
        :return:
        """
        raise NotImplementedError


class NoResponse(AbstractDialogueResponse):
    """
    NoResponse indicates that no response is expected of the conversation partner.
    """
    def get_response(self):
        # type: () -> str
        return ""


class BinaryResponse(AbstractDialogueResponse):
    """
    BinaryResponse is a response which the conversation partner gives by pressing one of two buttons. One button
    is labeled "yes" and the second is labeled "no".
    """

    BINARY_NO = "no"
    BINARY_YES = "yes"

    def get_response(self):
        # type: () -> str
        print("Waiting for user input...")

        get_button_response = get_srv_function('binary_button_input', BinaryButtonInput)

        return self.BINARY_YES if bool(get_button_response().response) else self.BINARY_NO


class AnyResponse(AbstractDialogueResponse):
    """
    AnyResponse indicates that we want the conversation partner to answer, but since there is no way to
    parse the answer of the conversation partner, we simply wait for silence.
    """

    def get_response(self):
        # type: () -> str
        time.sleep(3)  # TODO wait for silence
        return ""

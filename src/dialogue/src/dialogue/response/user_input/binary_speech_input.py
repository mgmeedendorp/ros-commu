from abstract_user_input import AbstractUserInput
from util import get_srv_function
from button_input.srv import BinaryButtonInput


class BinarySpeechInput(AbstractUserInput):
    """
    BinarySpeechInput is a response which the conversation partner gives by saying either yes or no.
     Currently implemented by the binary_button_input ros package, which handles this via the cli.
     #TODO: Make this voice-compatible
    """

    BINARY_NO = "no"
    BINARY_YES = "yes"

    def get_response(self):
        # type: () -> str
        print("Waiting for user input...")

        get_button_response = get_srv_function('binary_button_input', BinaryButtonInput)

        return self.BINARY_YES if bool(get_button_response().response) else self.BINARY_NO

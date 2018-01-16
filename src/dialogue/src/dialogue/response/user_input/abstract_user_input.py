from pocketsphinx import LiveSpeech

class AbstractUserInput:
    """
    AbstractUserInput is an abstract superclass that can be used to request input from the conversation partner
    (human person, usually) via the get_response function.
    """

    def get_response(self, live_speech):
        # type: (LiveSpeech) -> None
        """
        Blocks the thread until the conversation partner gives a response and returns that response.
        :param live_speech: A LiveSpeech instance to be used for speech input.
        :return: The response of the conversation partner
        """
        raise NotImplementedError

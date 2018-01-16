class AbstractUserInput:
    """
    AbstractUserInput is an abstract superclass that can be used to request input from the conversation partner
    (human person, usually) via the get_response function.
    """

    def get_response(self, sphinx_thread):
        # type: (PocketSphinxThread) -> None
        """
        Blocks the thread until the conversation partner gives a response and returns that response.
        :param sphinx_thread: A PocketSphinxThread instance to be used for speech input.
        :return: The response of the conversation partner
        """
        raise NotImplementedError

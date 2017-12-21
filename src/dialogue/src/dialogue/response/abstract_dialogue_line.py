from user_input import *


class AbstractDialogueLine:
    """
    AbstractDialogueLine is the basis of a Dialogue. It provides an utterance, an AbstractDialogueResponse to
    handle the response from the conversation partner and the next line of the script, which can be None, indicating the
    script is done.
    """

    def get_next_line(self, response):
        # type: (str) -> AbstractDialogueLine
        raise NotImplementedError

    def get_utterance(self):
        # type: () -> str
        raise NotImplementedError

    def request_user_response(self):
        # type: () -> AbstractUserInput
        raise NotImplementedError

    def can_cancel(self):
        # type: () -> bool
        """
        Whether the dialogue can be cancelled after uttering this line. (no cancelling after a question, for example).
        :return: Whether the dialogue can be cancelled after this line.
        """
        raise NotImplementedError
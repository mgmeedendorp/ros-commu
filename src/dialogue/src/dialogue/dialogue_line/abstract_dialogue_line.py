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
        raise NotImplementedError

    def can_cancel(self):
        # type: () -> bool
        """
        Whether the dialogue can be cancelled after uttering this line. (no cancelling after a question, for example).
        :return: Whether the dialogue can be cancelled after this line.
        """
        raise NotImplementedError

    def get_look_target(self, tf_talking_about):
        # type: (str) -> str
        """
        What the robot should look at while uttering this dialogue line.
        :param: The name of the tf_frame of the object that prompted this dialogue.
        :return: The name of a tf frame that the robot should be looking at. None for the default action of looking around.
        """
        raise NotImplementedError
from dialogue_input import NoResponse, BinaryResponse, AnyResponse


class Dialogue:
    """
    A Dialogue represents a conversation between CommU and a human as seen from CommU. The conversation structure is
    defined by an AbstractDialogueLine.

    """

    def __init__(self, dialogue_root):
        # type: (AbstractDialogueLine) -> None
        """
        :param dialogue_root: The first line of the conversation.
        """
        self.dialogue_root = dialogue_root
        self.current_line = dialogue_root
        self.should_cancel = False
        self.is_canceled = False

    def proceed_dialogue(self, utter):
        # type: (Callable[str, None]) -> bool
        """
        Proceed the dialogue to the next line by saying the next line, waiting for response and moving the pointer to
        current_line depending on the response.
        :param utter: a function that takes a string utterance as argument and makes CommU pronounce it.
        :return: Whether the dialogue was proceeded.
        """
        if not self.dialogue_remaining():
            return False

        utter(self.current_line.get_utterance())

        response = self.current_line.request_response().get_response()

        if self.should_cancel and self.current_line.can_cancel():
            self.is_canceled = True

        self.current_line = self.current_line.get_next_line(response)

        return True

    def dialogue_remaining(self):
        # type: () -> bool
        """
        Checks whether the dialogue is finished.
        :return: Whether there is a next line in the dialogue.
        """
        return self.current_line is not None and not self.is_canceled

    def reset_dialogue(self):
        # type: () -> None
        """
        Restarts the dialogue from the start.
        """
        self.current_line = self.dialogue_root
        self.should_cancel = False
        self.is_canceled = False

    def cancel_dialogue(self):
        # type: () -> None
        """
        Request to cancel this dialogue as soon as a DialogueLine is reached that can be canceled.
        """
        self.should_cancel = True


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

    def request_response(self):
        # type: () -> AbstractDialogueResponse
        raise NotImplementedError

    def can_cancel(self):
        # type: () -> bool
        """
        Whether the dialogue can be cancelled after uttering this line. (no cancelling after a question, for example).
        :return: Whether the dialogue can be cancelled after this line.
        """
        raise NotImplementedError


class DialogueLineNoResponse(AbstractDialogueLine):
    """
    DialogueLineNoResponse represents an utterance for which no answer is expected, and no time is given for a response.
    """

    def __init__(self, utterance, cancelable, next_line):
        # type: (str, bool, AbstractDialogueLine) -> None
        self.utterance = utterance
        self.next_line = next_line
        self.cancelable = cancelable

    def get_next_line(self, response) :
        # type: (str) -> AbstractDialogueLine
        return self.next_line

    def get_utterance(self):
        # type: () -> str
        return self.utterance

    def request_response(self):
        # type: () -> AbstractDialogueResponse
        return NoResponse()

    def can_cancel(self):
        return self.cancelable

class DialogueLineBinaryResponse(AbstractDialogueLine):
    """
    DialogueLineBinaryResponse indicates a simple yes/no question. It uses a BinaryResponse wait for user input and
    chooses the next line based on it.
    """

    def __init__(self, utterance, cancelable, next_line_yes, next_line_no):
        # type: (str, bool, AbstractDialogueLine, AbstractDialogueLine) -> None
        self.utterance = utterance
        self.next_line_yes = next_line_yes
        self.next_line_no = next_line_no
        self.cancelable = cancelable

    def get_next_line(self, response):
        # type: (str) -> AbstractDialogueLine
        if response == BinaryResponse.BINARY_YES:
            return self.next_line_yes
        return self.next_line_no

    def get_utterance(self):
        # type: () -> str
        return self.utterance

    def request_response(self):
        # type: () -> AbstractDialogueResponse
        return BinaryResponse()

    def can_cancel(self):
        return self.cancelable

class DialogueLineAnyResponse(DialogueLineNoResponse):
    """
    Wait for the conversation partner to finish talking after asking a question.
    """

    def request_response(self):
        # type: () -> AbstractDialogueResponse
        return AnyResponse()
import rospy
from response import *
from typing import Callable
from pocketsphinx import LiveSpeech


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

    def proceed_dialogue(self, utter, sphinx_thread):
        # type: (Callable[[str], None], PocketSphinxThread) -> bool
        """
        Proceed the dialogue to the next line by saying the next line, waiting for response and moving the pointer to
        current_line depending on the response.
        :param utter: a function that takes a string utterance as argument and makes CommU pronounce it.
        :param sphinx_thread: a PocketSphinxThread instance to be used for speech recognition.
        :return: Whether the dialogue was proceeded.
        """
        if not self.dialogue_remaining():
            return False

        utter(self.current_line.get_utterance())

        response = self.current_line.request_user_response().get_response(sphinx_thread)

        if self.should_cancel and self.current_line.can_cancel():
            rospy.loginfo("Dialogue cancelled.")
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

    def cancel_dialogue(self, next_topic):
        # type: (DialogueTopic) -> None
        """
        Request to cancel this dialogue as soon as a DialogueLine is reached that can be canceled.
        :param next_topic: The topic this one was cancelled for. Is None when the dialogue manager is shutdown.
        """
        rospy.loginfo("Dialogue cancel requested.")

        self.should_cancel = True
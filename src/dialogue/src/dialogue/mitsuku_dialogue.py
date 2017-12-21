import rospy
from typing import Callable
from dialogue import Dialogue
from chatbot import *
from pocketsphinx import LiveSpeech
from dialogue_manager import DialogueTopic

class MitsukuDialogue(Dialogue):
    """
    This is a special case of Dialogue, adapted for Mitsuku chatbot interaction.
    A Dialogue represents a conversation between CommU and a human as seen from CommU. The conversation structure is
    defined by an AbstractDialogueLine.
    """

    def __init__(self, audio_device):
        # type: (str) -> None
        """
        :param audio_device: The name of the audio device to use for input.
        """

        self.mitsuku = Mitsuku()
        self.livespeech = LiveSpeech(audio_device=audio_device, full_utt=True)

        self.should_cancel = False
        self.is_canceled = False
        self.next_topic = None # type: DialogueTopic

        self.previous_user_input = "Hi there!"

    def proceed_dialogue(self, utter):
        # type: (Callable[[str], None]) -> bool
        """
        Proceed the dialogue to the next line by saying the next line, waiting for response and moving the pointer to
        current_line depending on the response.
        :param utter: a function that takes a string utterance as argument and makes CommU pronounce it.
        :return: Whether the dialogue was proceeded.
        """
        if not self.dialogue_remaining():
            return False

        if self.should_cancel:
            if self.next_topic is not None:
                rospy.loginfo("Mitsuku dialogue cancelled. Switching to: " + self.next_topic.label)
                self.previous_user_input = "I want to talk about " + self.next_topic.label
            else:
                rospy.loginfo("Mitsuku dialogue cancelled. Switching to undefined next topic.")
                self.previous_user_input = "I want to talk about something else."

            self.is_canceled = True

        utter(self.mitsuku.getResponse(self.previous_user_input))

        user_input = self.livespeech.__iter__().next()

        self.previous_user_input = user_input

        return True

    def dialogue_remaining(self):
        # type: () -> bool
        """
        Checks whether the dialogue is finished.
        :return: Whether there is a next line in the dialogue.
        """
        return not self.is_canceled

    def reset_dialogue(self):
        # type: () -> None
        """
        Restarts the dialogue from the start.
        """
        self.should_cancel = False
        self.is_canceled = False
        self.next_topic = None

        self.mitsuku.refresh()

    def cancel_dialogue(self, next_topic):
        # type: (DialogueTopic) -> None
        """
        Request to cancel this dialogue as soon as a DialogueLine is reached that can be canceled.
        :param next_topic: The topic this one was cancelled for. Is None when the dialogue manager is shutdown.
        """
        rospy.loginfo("Dialogue cancel requested.")

        self.should_cancel = True
        self.next_topic = next_topic

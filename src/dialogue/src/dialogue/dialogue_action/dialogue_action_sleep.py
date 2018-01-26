import time

from __init__ import *
from typing import Union


class DialogueActionSleep(AbstractDialogueAction):
    """
    DialogueActionSleep adds a pause to the Dialogue.
    """

    def __init__(self, sleep_time, cancelable, next_action):
        # type: (int, bool, Union[AbstractDialogueAction, None]) -> None
        """
        :param sleep_time: The amount of seconds to wait.
        :param cancelable: Whether the dialogue can be cancelled after this DialogueAction.
        :param next_action: The next action in the Dialogue.
        """
        self.sleep_time = sleep_time
        self.cancelable = cancelable
        self.next_action = next_action

    def run(self, tf):
        # type: (str) -> AbstractDialogueAction
        """
        Use this function to perform an action and return the next action. Return None when there is no next action.
        :param tf: The name of the tf2_ros transform of the object that is currently being talked about.
        :return: The next action in the Dialogue. Return None when there is no next action.
        """
        time.sleep(self.sleep_time)

        return self.next_action

    def can_cancel(self):
        # type () -> bool
        """
        Whether the Dialogue can logically be cancelled after this DialogueAction.
        :return: Is this a good place in the Dialogue to stop if the Dialogue has to be cancelled?
        """
        return self.cancelable

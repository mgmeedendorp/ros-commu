from pocketsphinx import LiveSpeech
import threading
#https://github.com/bambocher/pocketsphinx-python


class PocketSphinxThread(threading.Thread):
    """
    A worker thread that takes runs Pocketsphinx to recognize words.

    https://eli.thegreenplace.net/2011/12/27/python-threads-communication-and-stopping

    Thread but also PocketSphinxHelper class that manages the thread. isListening event to control listening and a stoprequested event to stop the thread.
    """

    def __init__(self):
        self.listening = False
        self.listening_callback = None

    def start_listening(self, callback):
        # type: (Callable) -> None
        self.listening = True
        self.listening_callback = callback

    #def




if __name__ == "__main__":

    for phrase in LiveSpeech(): print(phrase)
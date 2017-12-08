from pocketsphinx import LiveSpeech
import threading
#https://github.com/bambocher/pocketsphinx-python


class PocketSphinxThread(threading.Thread):
    """
    A worker thread that takes runs Pocketsphinx to recognize words.
    """

    def __init__(self, callback):
        # type (Callable) -> PocketSphinxThread
        super(PocketSphinxThread, self).__init__()
        self.listening = threading.Event()
        self.stop_requested = threading.Event()
        self.listening_callback = callback

    def run(self):
        while not self.stop_requested.isSet():
            if self.listening.isSet():
                for phrase in LiveSpeech():
                    self.listening_callback(phrase)
                    break

    def start_listening(self):
        self.listening.clear()

    def stop_listening(self):
        self.listening.set()

    def stop_thread(self):
        self.stop_requested.set()



if __name__ == "__main__":

    for phrase in LiveSpeech(): print(phrase)
from pocketsphinx import LiveSpeech
import threading
from time import sleep
#https://github.com/bambocher/pocketsphinx-python


class PocketSphinxThread(threading.Thread):
    """
    A worker thread that takes runs Pocketsphinx to recognize words.
    """

    def __init__(self, callback, **pocketsphinx_options):
        # type (Callable) -> PocketSphinxThread
        super(PocketSphinxThread, self).__init__()
        self.live_speech = LiveSpeech(**pocketsphinx_options)

        self.pause_listening = threading.Event()
        self.stop_requested = threading.Event()
        self.listening_callback = callback

        self.__get_one_utterance_done = threading.Event()
        self.__get_one_utterance_result = ""

    def run(self):
        while not self.stop_requested.isSet():
            for phrase in self.live_speech:
                if not self.pause_listening.isSet() and not self.stop_requested.isSet():
                    self.listening_callback(phrase)
                    break

    def start_listening(self):
        self.pause_listening.clear()

    def stop_listening(self):
        self.pause_listening.set()

    def stop_thread(self):
        self.stop_requested.set()

    def is_listening(self):
        # type: () -> bool
        return not self.pause_listening.isSet() and not self.stop_requested.isSet()

    def get_one_utterance(self):
        # type: () -> str
        """
        A blocking function to wait for one utterance.
        :return: The utterance detected by PocketSphinx.
        """

        was_listening = self.is_listening()
        previous_listening_callback = self.listening_callback

        self.listening_callback = self.__get_one_utterance_callback

        if not was_listening:
            self.start_listening()

        self.__get_one_utterance_done.wait()

        self.listening_callback = previous_listening_callback

        if not was_listening:
            self.stop_listening()

        self.__get_one_utterance_done.clear()

        utterance = self.__get_one_utterance_result

        return utterance

    def __get_one_utterance_callback(self, utterance):
        self.__get_one_utterance_result = str(utterance)
        self.__get_one_utterance_done.set()


if __name__ == "__main__":
    def callback(utterance):
        print utterance

        #thread.stop_listening()
        #print "stop"

        #sleep(10)

        #thread.start_listening()
        #print "start"

    thread = PocketSphinxThread(callback, audio_device="alsa_input.usb-C-Media_Electronics_Inc._USB_PnP_Sound_Device-00.analog-mono")
    thread.start()

    sleep(30)

    thread.stop_thread()
    print "done"
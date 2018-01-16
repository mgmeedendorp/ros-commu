from pocketsphinx import LiveSpeech, Decoder
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

        if was_listening:
            self.stop_listening()

        utterance = ""

        for phrase in self.live_speech:
            utterance = phrase
            break

        if was_listening:
            self.start_listening()

        return utterance


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
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
        print "0"
        while not self.stop_requested.isSet():
            print "1"
            for phrase in self.live_speech:
                print "2"
                if self.pause_listening.isSet():
                    print "3"
                    self.listening_callback(phrase)
                    break

    def start_listening(self):
        self.pause_listening.clear()

    def stop_listening(self):
        self.pause_listening.set()

    def stop_thread(self):
        self.stop_requested.set()



if __name__ == "__main__":
    def callback(utterance):
        print utterance

        thread.stop_listening()

        sleep(10)

        thread.start_listening()

    thread = PocketSphinxThread(callback, audio_device="alsa_input.usb-C-Media_Electronics_Inc._USB_PnP_Sound_Device-00.analog-mono")
    thread.start()

    sleep(30)

    thread.stop_thread()
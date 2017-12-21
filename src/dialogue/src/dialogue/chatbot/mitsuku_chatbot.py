from mechanize import Browser
from bs4 import BeautifulSoup
import lxml


"""
This code was copied from https://github.com/Reinaesaya/OUIRL-ChatBot/blob/master/chatterbot/online_chatbots.py, with a new bot id.
"""

### Mitsuku ChatBot ###

MITSUKU_BOT_ID = "87437a824e345a0d"


class Mitsuku:
    def __init__(self):
        self.refresh()

    def refresh(self):
        self.br = Browser()
        self.br.set_handle_robots(False)
        response = self.br.open('https://kakko.pandorabots.com/pandora/talk?botid=%s&skin=chat' % (MITSUKU_BOT_ID))
        self.br_soup = BeautifulSoup(response.read(), "lxml")

        self.last_convohtml = str(self.br_soup.find('font', {'color': '#000000'}))
        self.all_messages = []
        self.last_message = None
        self.all_responses = []
        self.last_response = None

    def getResponse(self, message):
        # type: (str) -> str
        self.last_message = message
        self.all_messages.append(self.last_message)
        self.br.select_form(name='f')
        self.br.form['message'] = message

        response = self.br.submit()
        self.br_soup = BeautifulSoup(response.read(), "lxml")
        p = str(self.br_soup.find('font', {'color': '#000000'}))
        if self.last_convohtml == p:  # No response generated
            # print('Invalid input. Mitsuku had no answer')
            return None
        self.last_convohtml = p
        self.last_response = p.split('<br/> <br/>')[0].split('</b>')[-1].strip()
        # print(self.last_response.strip())
        self.last_response = self.removeTextWithinAngleBrackets(self.last_response)
        self.all_responses.append(self.last_response)

        return self.last_response

    def removeTextWithinAngleBrackets(self, text):
        new = ""
        left = 0
        for t in text:
            if t == '<':
                left += 1
                continue
            elif t == '>':
                left -= 1
                new = new + ' '
                continue

            if left < 0:
                print("Something went wrong in removing angle brackets")
                print(text)
                return text
            if left == 0:
                new = new + t
        return new.strip()

    def runSimulation(self):
        print('\n*------*')
        print('Welcome to the Mitsuku chatbot simulator on Python')
        print(
        'Implemented through use of mechanize library on https://kakko.pandorabots.com/pandora/talk?botid=%s&skin=chat' % (MITSUKU_BOT_ID))
        print('Original Mitsuku chatbot at www.mitsuku.com')
        print('To stop chat, Ctrl-C')
        print('*------*')

        try:
            while True:
                message = raw_input('\nEnter message: ')
                response = self.getResponse(message)
                if response is None:
                    print('Invalid input. Mitsuku had no answer')
                    continue
                print('Mitsuku: ' + response)
        except KeyboardInterrupt:
            print('\n*------*')
            print('Simulation ended.')
            print('*------*')


if __name__ == "__main__":
    mitsuku = Mitsuku()

    mitsuku.runSimulation()


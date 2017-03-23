import threading
import time

import os
import json
from os.path import join, dirname
#from dotenv import load_dotenv
from watson_developer_cloud import SpeechToTextV1 as SpeechToText
from watson_developer_cloud import AlchemyLanguageV1 as AlchemyLanguage
from core.components.game_event import *
from speech_sentiment_python.recorder import Recorder

from speech_dicts import *

class SpeechThread:

    def __init__(self):
        self.text = ""
        self.processing = False

    def add_observer(self, observer):
        self.observer = observer

    def transcribe_audio(self, path_to_audio_file):
        #username = os.environ.get("BLUEMIX_USERNAME")
        #password = os.environ.get("BLUEMIX_PASSWORD")
        username = "af3a03ef-27b9-49a6-94c4-04260b99a4b4"
        password = "kKsCsPRFfWYq"
        speech_to_text = SpeechToText(username=username,
                                      password=password)

        with open(path_to_audio_file, 'rb') as audio_file:
            return speech_to_text.recognize(audio_file,
                content_type='audio/wav')

    def start(self):
        t = threading.Thread(target=self.speech_thread)

        try:
            t.start()
        except (KeyboardInterrupt, SystemExit):
            t.stop()
            sys.exit()

    def get_last_text(self):
        return self.text

    def is_processing(self):
        return self.processing

    def speech_thread(self):
        filepath = os.getenv('APPDATA') + "/speech.wav";
        file = open(filepath, 'w+')
        file.close()
        while 1:
            try:
                #time.sleep(1)
                self.processing = False
                self.notify_observers()

                recorder = Recorder(filepath)

                print("Please say something nice into the microphone\n")
                recorder.record_to_file()

                self.processing = True
                self.notify_observers()

                print("Transcribing audio....\n")
                result = self.transcribe_audio(filepath)

                text = result['results'][0]['alternatives'][0]['transcript']
                self.text = text.strip()
                print("text is: " + self.text);

                self.processing = False
                self.notify_observers()


                parse_speech(self.text)
                #if (text == 'open' or text == 'okay'):
                #    print("matched event")
                #    pygame.event.post(pygame.event.Event(MENU_EVENT))

                print("Text: " + text + "\n")
            except IOError, e:
                print(e)
                print("IO error detected")
            except IndexError, e:
                print(e)
        return

    def notify_observers(self):
        print("NOTIFING")
        if (self.observer != None):
            self.observer.notify(self)

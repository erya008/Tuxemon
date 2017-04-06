
from core.components.game_event import *

import time
global numbers
global my_dict

speech_dictionary = {}

def add_speech_event(key, event):
    if (key in speech_dictionary):
        print("&&&&&&&&&&&&&&&&&&----COLLISION----" + key);
    else:
        speech_dictionary[key] = event;

def add_speech_event_plural(key, event):
    add_speech_event(key, event)
    add_speech_event(key + "s", event)

def parse_speech(text):
    print("TextKey: " + text)
    text_L = text.lower()
    words = text_L.split()
    for i in range (0, len(words)):
        if (words[i] in speech_dictionary):
            print("Posting: " + words[i])
            pygame.event.post(speech_dictionary[words[i]](words[i:]))
            break;

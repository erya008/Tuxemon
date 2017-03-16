from core.components.game_event import *
from main_dict import speech_dictionary

synonyms = ["stop"]

def stop_event(speech_text):
    return pygame.event.Event(STOP_EVENT)


for key in synonyms:
    speech_dictionary[key] = stop_event

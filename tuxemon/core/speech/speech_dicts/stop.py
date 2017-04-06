from core.components.game_event import *
from main_dict import add_speech_event

synonyms = ["stop"]

def stop_event(speech_text):
    return pygame.event.Event(STOP_EVENT)


for key in synonyms:
    add_speech_event(key, stop_event)

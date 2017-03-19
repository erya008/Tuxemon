from core.components.game_event import *
from main_dict import speech_dictionary

synonyms = ["open", "menu", "then you", "than you", "okay", "man you", "men you"]
monsters_synonyms = ["monsters", "monster"]
bag_synonyms = ["bag", "drag", "bad", "back"]
load_synonyms = ["load", "blowed"]
save_synonyms = ["save", "see", "say", "same"]
exit_synonyms = ["exit"]

def menu_event(speech_text):
    return pygame.event.Event(MENU_EVENT, action_name="open")

def monsters_event(speech_text):
    return pygame.event.Event(MENU_EVENT, action_name="monsters")

def bag_event(speech_text):
    return pygame.event.Event(MENU_EVENT, action_name="bag")

def load_event(speech_text):
    return pygame.event.Event(MENU_EVENT, action_name="load")

def save_event(speech_text):
    return pygame.event.Event(MENU_EVENT, action_name="save")

def exit_event(speech_text):
    return pygame.event.Event(MENU_EVENT, action_name="exit")

for key in synonyms:
    speech_dictionary[key] = menu_event

for key in monsters_synonyms:
    speech_dictionary[key] = monsters_event

for key in bag_synonyms:
    speech_dictionary[key] = bag_event

for key in load_synonyms:
    speech_dictionary[key] = load_event

for key in save_synonyms:
    speech_dictionary[key] = save_event

for key in exit_synonyms:
    speech_dictionary[key] = exit_event

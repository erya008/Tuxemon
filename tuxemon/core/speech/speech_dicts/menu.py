from core.components.game_event import *
from main_dict import speech_dictionary


synonyms = ["open", "menu", "then you", "than you", "okay", "man you", "men you"]
monsters_synonyms = ["monsters", "monster", "pokemon"]
bag_synonyms = ["bag", "drag", "bad", "back"]
load_synonyms = ["load", "blowed"]
save_synonyms = ["save", "see", "say", "same"]
exit_synonyms = ["exit"]


def open_world_menu_event(speech_text):
    return pygame.event.Event(OPEN_WORLD_MENU)

def monsters_event(speech_text):
    return pygame.event.Event(MENU_EVENT, target_menu=["world_menu", "combat_menu"], menu_item="monsters")

def bag_event(speech_text):
    return pygame.event.Event(MENU_EVENT, target_menu=["world_menu", "combat_menu"], menu_item="bag")

def load_event(speech_text):
    return pygame.event.Event(MENU_EVENT, target_menu=["world_menu", "combat_menu"], menu_item="load")

def save_event(speech_text):
    return pygame.event.Event(MENU_EVENT, target_menu=["world_menu", "combat_menu"], menu_item="save")

def exit_event(speech_text):
    return pygame.event.Event(MENU_EVENT, target_menu=["world_menu", "combat_menu"], menu_item="exit")

for key in synonyms:
    speech_dictionary[key] = open_world_menu_event

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

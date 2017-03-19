from core.components.game_event import *
from main_dict import speech_dictionary

synonyms = ["open", "menu", "then you", "okay", "man you", "men you"]
monsters_synonyms = ["monsters", "pokemon"]

def open_world_menu_event(speech_text):
    return pygame.event.Event(OPEN_WORLD_MENU)

def monsters_event(speech_text):
    return pygame.event.Event(MENU_EVENT, target_menu=["world_menu", "combat_menu"], menu_item="monsters")

for key in synonyms:
    speech_dictionary[key] = open_world_menu_event

for key in monsters_synonyms:
    speech_dictionary[key] = monsters_event

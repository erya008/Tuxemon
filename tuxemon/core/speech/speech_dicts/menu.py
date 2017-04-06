from core.components.game_event import *
from main_dict import add_speech_event, add_speech_event_plural


synonyms = ["open", "menu", "then you", "than you", "okay", "man you", "men you"]
close_menu_synonyms = ["close", "exit", "cancel"]
monsters_synonyms = ["monsters", "monster", "pokemon"]
bag_synonyms = ["bag", "drag", "bad", "back", "items", "item"]
load_synonyms = ["load", "blowed"]
slot1_synonyms = ["one", "won"]
slot2_synonyms = ["two", "to", "too"]
save_synonyms = ["save", "see", "say", "same"]


def open_world_menu_event(speech_text):
    return pygame.event.Event(OPEN_WORLD_MENU)

def close_menu_event(speech_text):
    return pygame.event.Event(MENU_EVENT, target_menu=["world_menu", "combat_menu"], menu_item="close")

def monsters_event(speech_text):
    return pygame.event.Event(MENU_EVENT, target_menu=["world_menu", "combat_menu"], menu_item="monsters")

def bag_event(speech_text):
    return pygame.event.Event(MENU_EVENT, target_menu=["world_menu", "combat_menu"], menu_item="bag")

def load_event(speech_text):
    return pygame.event.Event(MENU_EVENT, target_menu=["world_menu"], menu_item="load")

def slot1_event(speech_text):
    return pygame.event.Event(MENU_EVENT, target_menu=["world_menu"], menu_item="slot one")

def slot2_event(speech_text):
    return pygame.event.Event(MENU_EVENT, target_menu=["world_menu"], menu_item="slot two")

def save_event(speech_text):
    return pygame.event.Event(MENU_EVENT, target_menu=["world_menu"], menu_item="save")

def exit_event(speech_text):
    return pygame.event.Event(MENU_EVENT, target_menu=["world_menu"], menu_item="exit")

for key in synonyms:
    add_speech_event(key, open_world_menu_event)

for key in close_menu_synonyms:
    add_speech_event(key, close_menu_event)

for key in monsters_synonyms:
    add_speech_event(key, monsters_event)

for key in bag_synonyms:
    add_speech_event(key, bag_event)

for key in load_synonyms:
    add_speech_event(key, load_event)

for key in slot1_synonyms:
    add_speech_event(key, slot1_event)

for key in slot2_synonyms:
    add_speech_event(key, slot2_event)

for key in save_synonyms:
    add_speech_event(key, save_event)

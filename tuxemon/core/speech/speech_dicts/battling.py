from core.components.game_event import *
from main_dict import speech_dictionary

fight_synonyms = ["fight", "battle", "go"]
run_synonyms = ["run", "bye", "not again", "see you"]
swap_synonyms = ["return", "come back", "swap"]
move_synonyms = ["bite"]
potion_synonyms = ["super", "potion", "super potion"]

def fight_event(speech_text):
    return pygame.event.Event(MENU_EVENT, target_menu = ["combat_menu"], menu_item = "fight")
def run_event(speech_text):
    print("CREATED A RUN EVENT")
    return pygame.event.Event(MENU_EVENT, target_menu = ["combat_menu"], menu_item = "run")
def swap_event(speech_text):
    return pygame.event.Event(MENU_EVENT, target_menu = ["combat_menu"], menu_item = "swap")
def move_event(speech_text):
    return pygame.event.Event(MENU_EVENT, target_menu = ["technique_menu"], menu_item = "bite")
def potion_event(speech_text):
    return pygame.event.Event(MENU_EVENT, target_menu = ["item_menu"], menu_item = "super potion")

for key in fight_synonyms:
    speech_dictionary[key] = fight_event
for key in run_synonyms:
    speech_dictionary[key] = run_event
for key in swap_synonyms:
    speech_dictionary[key] = swap_event
for key in move_synonyms:
    speech_dictionary[key] = move_event
for key in potion_synonyms:
    speech_dictionary[key] = potion_event

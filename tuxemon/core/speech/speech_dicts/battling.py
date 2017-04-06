from core.components.game_event import *
from main_dict import add_speech_event, add_speech_event_plural

fight_synonyms = ["fight", "battle", "go"]
run_synonyms = ["run", "not again", "see you", "away"]
swap_synonyms = ["return", "come back", "swap"]

def fight_event(speech_text):
    return pygame.event.Event(MENU_EVENT, target_menu = ["combat_menu"], menu_item = "fight")
def run_event(speech_text):
    print("CREATED A RUN EVENT")
    return pygame.event.Event(MENU_EVENT, target_menu = ["combat_menu"], menu_item = "run")
def swap_event(speech_text):
    return pygame.event.Event(MENU_EVENT, target_menu = ["combat_menu"], menu_item = "swap")
def items_event(speech_text):
    return pygame.event.Event(MENU_EVENT, target_menu = ["combat_menu"], menu_item = "item")

for key in fight_synonyms:
    add_speech_event(key, fight_event)
for key in run_synonyms:
    add_speech_event(key, run_event)
for key in swap_synonyms:
    add_speech_event(key, swap_event)
#for key in items_synonyms:
#    add_speech_event_plural(key, items_event)

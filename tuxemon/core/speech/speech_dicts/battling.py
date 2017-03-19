from core.components.game_event import *
from main_dict import speech_dictionary

fight_synonyms = ["fight", "battle", "go"]
item_synonyms = ["bag", "items", "item"]
run_synonyms = ["run", "bye", "not again", "see you"]
swap_synonyms = ["return", "come back", "swap"]

def fight_event(speech_text):
    return pygame.event.Event(BATTLE_EVENT, action_name="fight")
def item_event(speech_text):
    return pygame.event.Event(BATTLE_EVENT, action_name="item")
def run_event(speech_text):
    print("CREATED A RUN EVENT")
    return pygame.event.Event(BATTLE_EVENT, action_name="run")
def swap_event(speech_text):
    return pygame.event.Event(BATTLE_EVENT, action_name="swap")

for key in fight_synonyms:
    speech_dictionary[key] = fight_event
for key in item_synonyms:
    speech_dictionary[key] = item_event
for key in run_synonyms:
    speech_dictionary[key] = run_event
for key in swap_synonyms:
    speech_dictionary[key] = swap_event

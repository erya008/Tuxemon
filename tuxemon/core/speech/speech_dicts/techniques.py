from core.components.game_event import *
from main_dict import speech_dictionary

bite_synonyms = ["bite", "fight", "might", "by"]
pound_synonyms = ["pound", "mound", "round", "ow"]
water_shot_synonyms = ["water", "shot", "dot", "pot"]

def bite_event(speech_text):
    return pygame.event.Event(MENU_EVENT, target_menu = ["technique_menu"], technique_name = "bite")
def pound_event(speech_text):
    return pygame.event.Event(MENU_EVENT, target_menu = ["technique_menu"], technique_name = "pound")
def water_shot_event(speech_text):
    return pygame.event.Event(MENU_EVENT, target_menu = ["technique_menu"], technique_name = "water")

for key in bite_synonyms:
    speech_dictionary[key] = bite_event
for key in pound_synonyms:
    speech_dictionary[key] = pound_event
for key in water_shot_synonyms:
    speech_dictionary[key] = water_shot_event

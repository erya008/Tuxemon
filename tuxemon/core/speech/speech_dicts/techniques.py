from core.components.game_event import *
from main_dict import add_speech_event, add_speech_event_plural

bite_synonyms = ["spite", "bite", "might", "by"]
pound_synonyms = ["pound", "mound", "round", "ow"]
water_shot_synonyms = ["water", "shot", "dot", "pot"]

def bite_event(speech_text):
    return pygame.event.Event(MENU_EVENT, target_menu = ["technique_menu"], technique_name = "Bite")
def pound_event(speech_text):
    return pygame.event.Event(MENU_EVENT, target_menu = ["technique_menu"], technique_name = "Pound")
def water_shot_event(speech_text):
    return pygame.event.Event(MENU_EVENT, target_menu = ["technique_menu"], technique_name = "Water Shot")

for key in bite_synonyms:
    add_speech_event_plural(key, bite_event)
for key in pound_synonyms:
    add_speech_event_plural(key, pound_event)
for key in water_shot_synonyms:
    add_speech_event_plural(key, water_shot_event)

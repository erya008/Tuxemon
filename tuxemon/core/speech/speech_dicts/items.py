from core.components.game_event import *
from main_dict import speech_dictionary

potion_synonyms = ["super", "duper", "potion", "lotion", "motion", "loop", "ocean"]
ball_synonyms = ["ball", "call", "fall", "capture", "device", "advice", "rapture"]

def potion_event(speech_text):
    return pygame.event.Event(MENU_EVENT, target_menu = ["items_menu"], item_name = "Super Potion")
def ball_event(speech_text):
    return pygame.event.Event(MENU_EVENT, target_menu = ["items_menu"], item_name = "Capture Device")

for key in potion_synonyms:
    speech_dictionary[key] = potion_event
    speech_dictionary[key + "s"] = potion_event
for key in ball_synonyms:
    speech_dictionary[key] = ball_event
    speech_dictionary[key + "s"] = ball_event

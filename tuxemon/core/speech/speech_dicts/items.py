from core.components.game_event import *
from main_dict import add_speech_event, add_speech_event_plural

potion_synonyms = ["super", "duper", "potion", "lotion", "motion", "loop", "ocean"]
ball_synonyms = ["ball", "call", "fall", "capture", "captured", "device", "advice", "rapture"]

def potion_event(speech_text):
    return pygame.event.Event(MENU_EVENT, target_menu = ["items_menu"], item_name = "Super Potion")
def ball_event(speech_text):
    return pygame.event.Event(MENU_EVENT, target_menu = ["items_menu"], item_name = "Capture Device")

for key in potion_synonyms:
    add_speech_event_plural(key, potion_event)
for key in ball_synonyms:
    add_speech_event_plural(key, ball_event)

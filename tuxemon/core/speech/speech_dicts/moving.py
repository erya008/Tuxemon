from core.components.game_event import *
from main_dict import speech_dictionary
import time



north_synonyms  = ["north","northbound","up"]
east_synonyms   = ["east","eastbound","he's","right"]
south_synonyms  = ["south", "now","so","southbound","down"]
west_synonyms   = ["west","westbound","left"]

wander_synonyms = ["wander", "wonder"]

number_dict ={"one":1,
    "two":2,
    "to":2,
    "too":2,
    "three":3,
    "four":4,
    "five":5,
    "six":6,
    "seven":7}


def north_event():
    return pygame.event.Event(COMPLEX_MOVE_EVENT, move_list = ["N","N","N","N","N"])

def east_event():
    return pygame.event.Event(COMPLEX_MOVE_EVENT, move_list = ["E","E","E","E","E","E","E","E"])

def south_event():
    return pygame.event.Event(COMPLEX_MOVE_EVENT, move_list = ["S","S","S","S","S"])

def west_event():
    return pygame.event.Event(COMPLEX_MOVE_EVENT, move_list = ["W","W","W","W","W","W","W","W"])

def wander_event(speech_text):
    return pygame.event.Event(COMPLEX_MOVE_EVENT, move_list = ["N", "E", "S", "W","N", "E", "S", "W","N", "E", "S", "W","N", "E", "S", "W","N", "E", "S", "W","N", "E", "S", "W"])

def move_event(speech_text):
    list_of_moves = []
    current_state = ""
    continuous_move = True
    for word in speech_text:
        print(word)
        if (word.lower() in north_synonyms):
            current_state = "N"
        elif (word.lower() in south_synonyms):
            current_state = "S"
        elif (word.lower() in east_synonyms):
            current_state = "E"
        elif (word.lower() in west_synonyms):
            current_state = "W"
        elif (word.lower() in number_dict):
            continuous_move = False
            for i in range (0, number_dict[word.lower()]):
                list_of_moves.append(current_state)
        else:
            break
    if (continuous_move):
        if (current_state == "N"):
            return north_event()
        elif (current_state == "S"):
            return south_event()
        elif (current_state == "E"):
            return east_event()
        elif (current_state == "W"):
            return west_event()
    else:
        print("found a move list")
        print(list_of_moves)
        return pygame.event.Event(COMPLEX_MOVE_EVENT, move_list=list_of_moves)

for key in wander_synonyms:
    speech_dictionary[key] = wander_event

for key in north_synonyms:
    speech_dictionary[key] = move_event


for key in east_synonyms:
    speech_dictionary[key] = move_event


for key in south_synonyms:
    speech_dictionary[key] = move_event


for key in west_synonyms:
    speech_dictionary[key] = move_event

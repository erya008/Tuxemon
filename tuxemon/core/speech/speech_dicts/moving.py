from core.components.game_event import *
from main_dict import speech_dictionary
import time



north_synonyms  = ["north","northbound","up"]
east_synonyms   = ["east","eastbound","he's","right"]
south_synonyms  = ["south", "now","so","southbound","down"]
west_synonyms   = ["west","westbound","left"]




def stopwatch(seconds):
    start = time.time()
    time.clock()
    elapsed = 0
    while elapsed < seconds:
        elapsed = time.time() - start
        pygame.event.Event(NORTH_EVENT)

        print "loop cycle time: %f, seconds count: %02d" % (time.clock() , elapsed)
        time.sleep(1)

def north_event(speech_text):

    return pygame.event.Event(NORTH_EVENT)


def east_event(speech_text):
    return pygame.event.Event(EAST_EVENT)

def south_event(speech_text):
    return pygame.event.Event(SOUTH_EVENT)

def west_event(speech_text):
    return pygame.event.Event(WEST_EVENT)





for key in north_synonyms:
    speech_dictionary[key] = north_event


for key in east_synonyms:
    speech_dictionary[key] = east_event


for key in south_synonyms:
    speech_dictionary[key] = south_event


for key in west_synonyms:
    speech_dictionary[key] = west_event

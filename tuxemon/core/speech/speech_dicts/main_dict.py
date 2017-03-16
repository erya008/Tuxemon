
from core.components.game_event import *

import time
global numbers
global my_dict
my_dict ={"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7}


speech_dictionary = {}
def stopwatch(seconds):
    start = time.time()
    time.clock()
    elapsed = 0
    while elapsed < seconds:
        elapsed = time.time() - start
        pygame.event.Event(NORTH_EVENT)

        print "loop cycle time: %f, seconds count: %02d" % (time.clock() , elapsed)
        time.sleep(1)
def numb(var):
    global t
    global enter
    print(enter)

    if ( var =='one') :
        t=1
        print(var)
        enter = True
        return
    if( var =='two'):
        t=2
        print(var)
        enter = True
        return
    if( var =='three'):
        t=3
        print(var)
        enter = True
        return






def parse_speech(text):
    print("TextKey: " + text)
    text_L = text.lower()
    words = text_L.split()
    for word in words:
        if (word in speech_dictionary):
            pygame.event.post(speech_dictionary[word](text))

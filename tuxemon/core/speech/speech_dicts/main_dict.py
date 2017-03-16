
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






def parse_speech(textKey, text):
    global t
    global numbers
    global my_dict
    i=0
    textKey_L = textKey.lower()
    words = textKey_L.split()
    for i in range(0,2):
    #for word in numbers:
    #    if word in numbers:
            #numb(word)
        for word in words:
            if word in my_dict:

                     t=int(my_dict[word])
                     print("hello")
                     print(t)
            if word in speech_dictionary:
                    print(word)
                    start = time.time()
                    start1=int(round(time.time() * 1000))
                    time.clock()
                    elapsed = 0
                    seconds=10*t*10
                    while elapsed < seconds:
                        print(seconds)
                        elapsed = int(round(time.time() * 1000)) -start1
                        pygame.event.post(speech_dictionary[word](text))

                        print(t)
                        print "loop cycle time: %f, seconds count: %02d" % (time.clock() , elapsed)
                        time.sleep(.1*t)
                    pygame.event.post(pygame.event.Event(STOP_EVENT))
                    i+=1

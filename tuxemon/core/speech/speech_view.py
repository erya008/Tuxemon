import pygame
from core import prepare
from threading import Timer
from time import sleep
import time
class SpeechView:
    screen_text = "no speech text here"


    def __init__(self):
        self.font_color = (255,140,0)
        self.font = pygame.font.SysFont('Arial', 36, bold=True)
        self.voice_text = ""
        self.dot_count = 0;
        self.processing = False;
        self.control_dots()
        self.processing_sprite = [None] * 10
        self.mic_image = pygame.image.load(prepare.BASEDIR + "resources/interface/listening.png")
        for i in range(0,9):
            self.processing_sprite[i] = pygame.image.load(prepare.BASEDIR + "resources/interface/proc"+str(i)+".png")


    def draw(self, screen):
        #screen.blit(self.font.render(self.voice_text, True, self.font_color), (100,550))


        if (self.processing):
            for i in range(0,9):
                screen.blit(self.processing_sprite[i], (100,500))
                sleep(0.1)
        else:
            #screen.blit(self.font.render("Listening...", True, self.font_color), (100,600))
            screen.blit(self.mic_image, (100,500))
        #print("Drawing inside speech view")

    def notify(self, other):
        print("was notified")
        self.voice_text = other.get_last_text()
        self.processing = other.is_processing()

    def get_dot_text(self):
        output = "Processing speech"
        for i in range(self.dot_count):
            output = output + "."

        return output

    def control_dots(self):
        self.dot_count = self.dot_count + 1;
        if (self.dot_count == 4):
            self.dot_count = 1;
        Timer(0.3, self.control_dots).start()

import pygame
from threading import Timer
class SpeechView:
    screen_text = "no speech text here"

    def __init__(self):
        self.voice_text = ""
        self.dot_count = 0;
        self.processing = False;
        self.control_dots()
        self.font = pygame.font.SysFont('Arial', 36)


    def draw(self, screen):

        screen.blit(self.font.render(self.voice_text, True, (0,0,0)), (200, 100))


        if (self.processing):
            screen.blit(self.font.render(self.get_dot_text(), True, (0,0,0)), (200, 150))
        else:
            screen.blit(self.font.render("Listening...", True, (0,0,0)), (200, 150))
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

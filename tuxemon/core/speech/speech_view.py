import pygame

class SpeechView:
    screen_text = "no speech text here"

    def __init__(self):
        self.voice_text = "no previous voice text"

    def draw(self, screen):
        self.font = pygame.font.SysFont('Arial', 36)
        screen.blit(self.font.render(self.voice_text, True, (0,0,0)), (200, 100))
        #print("Drawing inside speech view")

    def notify(self, other):
        print("was notified")
        self.voice_text = other.get_last_text()

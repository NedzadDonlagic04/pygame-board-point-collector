import pygame

class MyClock:
    def __init__(self, fps):
        self.CLOCK = pygame.time.Clock()
        self.FPS = fps

    def tick(self):
        self.CLOCK.tick(self.FPS)
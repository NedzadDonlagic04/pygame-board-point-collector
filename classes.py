import pygame

class MyClock:
    def __init__(self, fps):
        self.CLOCK = pygame.time.Clock()
        self.FPS = fps

    def tick(self):
        self.CLOCK.tick(self.FPS)

class Player(pygame.sprite.Sprite):
    def __init__(self, rectWidth, rectHeight, screenWidth, screenHeight, color=[0, 0, 0]):
        super().__init__()
        self.image = pygame.Surface((rectWidth, rectHeight), pygame.SRCALPHA)
        pygame.draw.rect(self.image, color, (0, 0, rectWidth, rectHeight), border_radius=10)
        self.rect = self.image.get_rect( center = (screenWidth / 2, screenHeight - 50) )

        self.SCREEN_WIDTH = screenWidth
        self.SPEED = 5
    
    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.left -= self.SPEED

            if self.rect.left < 0:
                self.rect.left = 0
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.right += self.SPEED

            if self.rect.right > self.SCREEN_WIDTH:
                self.rect.right = self.SCREEN_WIDTH
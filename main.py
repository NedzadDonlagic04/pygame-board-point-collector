import pygame
from sys import exit
from classes import *

class Game:
    def __init__(self, width, height, title):
        pygame.init()

        self.WIDTH = width
        self.HEIGHT = height
        self.SCREEN = pygame.display.set_mode((width, height))
        self.SCREEN_BG = 'white'
        
        pygame.display.set_caption(title)

        self.CLOCK = MyClock(60)

        self.PLAYER = pygame.sprite.GroupSingle( Player(100, 20, width, height) )

        self.BLOCKS = pygame.sprite.Group( Block(80, 50, width, height) )

        self.SCORE = Score(50)
    
    def quit(self):
        pygame.quit()
        exit()
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
            
            self.SCREEN.fill(self.SCREEN_BG)

            self.PLAYER.update()
            self.PLAYER.draw(self.SCREEN)

            self.BLOCKS.update(self.SCORE)
            self.BLOCKS.draw(self.SCREEN)

            self.SCORE.update(self.PLAYER.sprite, self.BLOCKS)
            self.SCORE.draw(self.SCREEN)

            if self.SCORE.GAME_OVER:
                self.quit()

            for block in self.BLOCKS:
                if block.rect.bottom == self.HEIGHT / 3:
                    self.BLOCKS.add(Block(80, 50, self.WIDTH, self.HEIGHT, self.SCORE.score))
                    break

            pygame.display.update()
            self.CLOCK.tick()

if __name__ == '__main__':
    game = Game(800, 600, 'Point Collector')
    game.run()
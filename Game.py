'''
Created on Jan 30, 2015

@author: Jeremy
'''

import pygame
import sys
from random import randint, choice


from Player import Player
from Food import Food

class Game(object):
    def __init__(self, screen):
        clock = pygame.time.Clock()
        self.foodGroup = pygame.sprite.Group()
        self.initFood()
        self.player = Player()
        

        while True:
            dt = clock.tick(60)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                if event.type == pygame.KEYDOWN:
                    if self.player.keydown(event):
                            continue
                elif event.type == pygame.KEYUP:
                    if self.player.keyup(event):
                            continue

            self.player.update(dt / 1000.0)
            self.foodGroup.update(dt / 1000.0)
            screen.fill((200, 200, 200))
            self.foodGroup.draw(screen)
            self.player.draw(screen)
            pygame.display.flip()
            
    def initFood(self):
        for x in range(0, 100):
            xDir = choice((-1, 1))
            yDir = choice((-1, 1))
            self.foodGroup.add(Food(randint(4, 16), randint(40, 600), randint(40, 400), randint(60, 100)*xDir, randint(60, 100)*yDir, 640, 480, randint(1, 255), randint(1, 255), randint(1, 255), self.foodGroup))
            
        

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Cube Man")
    screen = pygame.display.set_mode((640,480))
    Game(screen)
    


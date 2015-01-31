'''
Created on Jan 30, 2015

@author: Jeremy
'''
import pygame

class Food(pygame.sprite.Sprite): 
    def __init__(self, size, x, y, xVel, yVel, xBound, yBound, r, g, b, *foodGroup):
        self.size = size
        self.x = x
        self.y = y
        self.xVel = xVel
        self.yVel = yVel
        self.xBound = xBound
        self.yBound = yBound
        self.r = r
        self.g = g
        self.b = b
        pygame.sprite.Sprite.__init__(self, foodGroup)
        
        self.image = pygame.Surface((size, size))
        self.image.fill((r, g, b))
        self.rect = pygame.rect.Rect((x,y), (size, size))
        
    def update(self, dt):
        if self.rect.x > self.xBound-self.size or self.rect.x <= 0:
            self.xVel *= -1
        if self.rect.y > self.yBound-self.size or self.rect.y <= 0:
            self.yVel *= -1
            
        self.rect.x += self.xVel * dt
        self.rect.y += self.yVel * dt

    
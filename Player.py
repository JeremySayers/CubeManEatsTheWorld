'''
Created on Jan 30, 2015

@author: Jeremy
'''

import pygame

class Player(pygame.sprite.Sprite):    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.__group = pygame.sprite.GroupSingle()
        self.__group.add(self)
        self.image = pygame.image.load('GrassTile.png')
        self.rect = pygame.rect.Rect((320,240), self.image.get_size())
        
        self.up = False 
        self.down = False 
        self.right  = False
        self.left = False
    
    def draw(self, surface):
        self.__group.draw(surface)
    
    def update(self, dt):
        if self.left:
            self.rect.x -= 300 * dt
        if self.right:
            self.rect.x += 300 * dt
        if self.up:
            self.rect.y -= 300 * dt
        if self.down:
            self.rect.y += 300 * dt

    def keydown(self, event):
        result = False
        if event.key == pygame.K_a:
            self.left = True
            result = True
        elif event.key == pygame.K_d:
            self.right = True
            result = True
        elif event.key == pygame.K_w:
            self.up = True
            result = True
        elif event.key == pygame.K_s:
            self.down = True
            result = True
        
        return result
            
    def keyup(self, event):
        result = False
        if event.key == pygame.K_a:
            self.left = False
            result = True
        elif event.key == pygame.K_d:
            self.right = False
            result = True
        elif event.key == pygame.K_w:
            self.up = False
            result = True
        elif event.key == pygame.K_s:
            self.down = False
            result = True
            
        return result
        
        
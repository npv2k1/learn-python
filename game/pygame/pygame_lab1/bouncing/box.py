import pygame
import random

class Box:
    def __init__(self, x, y, w, h) -> None:
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speedX = 1
        self.speedY = 1
        pass

    def draw(self, surface):
        self.x += self.speedX
        self.y += self.speedY
        pygame.draw.rect(surface, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), (self.x, self.y, self.w, self.h))

    def move_up(self):
        self.speedY -= 1

    def move_down(self):
        self.speedY += 1

    def move_right(self):
        self.speedX += 1

    def move_left(self):
        self.speedX -= 1

    def check_wall(self):
        if(self.x < 0):
           
            self.x = 0

        if (self.y < 0):
            
            self.y = 0
        if(self.x > pygame.display.get_surface().get_size()[0] - self.w):
           
            self.x = pygame.display.get_surface().get_size()[0] - self.w
        if(self.y > pygame.display.get_surface().get_size()[1] - self.h):
            
            self.y = pygame.display.get_surface().get_size()[1] - self.h

    def bouncing(self):
        if(self.x < 0):
           
           self.speedX=-self.speedX

        if (self.y < 0):
            self.speedY=-self.speedY
            
            
        if(self.x > pygame.display.get_surface().get_size()[0] - self.w):
           
             self.speedX=-self.speedX
        if(self.y > pygame.display.get_surface().get_size()[1] - self.h):
            self.speedY=-self.speedY
            
            
    def move(self):
        self.x += random.randint(-5,5)
        self.y += random.randint(-5,5)

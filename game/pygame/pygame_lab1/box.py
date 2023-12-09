import pygame
import random
pygame.font.init()
myfont = pygame.font.SysFont('Fira Code', 30)


class Box:
    def __init__(self, x, y, w, h, text) -> None:
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speedX = 0
        self.speedY = 0
        self.text = text
        self.color = (random.randint(0, 255), random.randint(
            0, 255), random.randint(0, 255))
        self.textColor = (random.randint(0, 255), random.randint(
            0, 255), random.randint(0, 255))
        pass

    def draw(self, surface):
        self.x += self.speedX
        self.y += self.speedY

        textsurface = myfont.render(self.text, False,  self.textColor)

        pygame.draw.rect(surface, self.color, (self.x, self.y, self.w, self.h))

        surface.blit(textsurface, (self.x+10, self.y+15))

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

            self.speedX = -self.speedX

        if (self.y < 0):
            self.speedY = -self.speedY

        if(self.x > pygame.display.get_surface().get_size()[0] - self.w):

            self.speedX = -self.speedX
        if(self.y > pygame.display.get_surface().get_size()[1] - self.h):
            self.speedY = -self.speedY

    def move(self):
        self.x += random.randint(-5, 5)
        self.y += random.randint(-5, 5)

    def check_click(self, pos):
        if(pos[0] >= self.x and pos[0] <= self.x+self.w and pos[1] >= self.y and pos[1] <= self.y+self.h):
            return True

        return False

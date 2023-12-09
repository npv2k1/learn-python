import pygame
import random
import box
import random
# init
pygame.init()
pygame.font.init()  # you have to call this at the start,
# if you want to use this module.


# # create the screen
screen = pygame.display.set_mode((800, 600))


# DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)


list_box = []
for i in range(100):
    list_box.append(box.Box(random.randint(20, 700),
                    random.randint(20, 500), 40, 40, str(i)))


# Game loop
running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # print(event.pos)
            for bb in list_box:
                if(bb.check_click(event.pos)):

                    list_box.remove(bb)

    for bb in list_box:
        # bb.bouncing()
        bb.check_wall()
        # bb.move()
        bb.draw(screen)
    # print('\r', b.x, b.y, b.speedX,b.speedY, end='')

    pygame.display.update()

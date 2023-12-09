import pygame

# init
pygame.init()
pygame.font.init()  # you have to call this at the start,
# if you want to use this module.


# # create the screen
screen = pygame.display.set_mode((800, 600))


# DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)



# Game loop
running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # print(event.pos)
            pass

    pygame.display.update()
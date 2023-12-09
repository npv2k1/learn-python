import pygame
import random
import box
import random
# init
pygame.init()
pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
# myfont = pygame.font.SysFont('Comic Sans MS', 30)
# textsurface = myfont.render('Some Text', False, (255, 0, 0))

# # create the screen
screen = pygame.display.set_mode((800, 600))
# background
# background = pygame.image.load('background.jpg')

# # title and icon
# pygame.display.set_caption('Space invaders')
# icon = pygame.image.load('ufo.png')
# pygame.display.set_icon(icon)

# # Player
# playerImg = pygame.image.load('player.png')
# playerX = 370
# playerY = 480
# playerX_change = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def fire_bullet(x, y):
    global bulletY_state
    bulletY_state = 'fire'
    screen.blit(bulletImg, (x+16, y+10))


print(pygame.FULLSCREEN)
DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
b = box.Box(5, 5, 100, 100)

list_box=[]
for i in range(1000):
    list_box.append(box.Box(random.randint(1,799),random.randint(1,799),10,10))



# Game loop
running = True
while running:
    screen.fill((0, 0, 0))
    b.check_wall()
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
       
        # if keystroke is press
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                b.move_left()

            if event.key == pygame.K_RIGHT:
                b.move_right()

            if event.key == pygame.K_UP:
                b.move_up()

            if event.key == pygame.K_DOWN:
                b.move_down()

        if event.type == pygame.KEYUP:
            b.speedX=0
            b.speedY=0

    # b.move_down()
    # check bonu
    for bb in list_box:
        bb.bouncing()
        bb.check_wall()
        bb.move()
        bb.draw(screen)
    # print('\r', b.x, b.y, b.speedX,b.speedY, end='')
    
    # bullet

    # update screen
    pygame.display.update()

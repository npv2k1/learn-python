import pygame
import random

# init
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))
# background
background = pygame.image.load('background.jpg')

# title and icon
pygame.display.set_caption('Space invaders')
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0
# Enemy
enemyImg = pygame.image.load('enemy.png')
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 0.3
enemyY_change = 20

# bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 500
bulletY = 600
bulletX_change = 0
bulletY_change = 0.2
bulletY_state = 'ready'


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def fire_bullet(x, y):
    global bulletY_state
    bulletY_state = 'fire'
    screen.blit(bulletImg, (x+16, y+10))


# Game loop
running = True
while running:
    # RGB
    screen.fill((0, 0, 0))
    # background image

    screen.blit(background, (0, 0))
    pygame.draw.line(screen, (0, 255, 0), (0, 0), (100, 100))
    pygame.draw.line(screen, (0, 255, 0), (100, 0), (100, 100))
    pygame.draw.rect(screen,(0,0,0),(100,100,50,20))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is press
        if event.type == pygame.KEYDOWN:
            print("down")

            if event.key == pygame.K_LEFT:
                playerX_change -= 0.2

            if event.key == pygame.K_RIGHT:
                playerX_change += 0.2

            if event.key == pygame.K_SPACE:
                print("bullet")
                fire_bullet(playerX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
                print('up')

    # print('\r',playerX_change,end='')

    # check bonu
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    enemyX += enemyX_change
    if enemyX <= 0:
        enemyX_change = 0.3
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -0.3
        enemyY += enemyY_change

    # bullet
    if (bulletY_state == 'fire'):
        fire_bullet(playerX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    enemy(enemyX, enemyY)

    # update screen
    pygame.display.update()

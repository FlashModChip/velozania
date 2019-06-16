import pygame, sys
from pygame.locals import *
from random import randrange, randint

pygame.init()

FPS = 30
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption('Animation')

BLACK = (250, 250, 250)
GREEN = (0, 255, 0)
STREET = (150, 150, 150)
DISPLAYSURF.fill(BLACK)

pygame.draw.rect(DISPLAYSURF, GREEN, (0, 450, 800, 50))

redcarImg = pygame.image.load('images/redcar.png')
redcar_rect = redcarImg.get_rect()

cyclerImg = pygame.image.load('images/Cycler.png')
cyclerImg = pygame.transform.scale(cyclerImg, (100, 70))
cyclerx = 40
cyclery = 350

slow = cyclery

j = randint(100, 400)

k = 900

while True:
    if k > -100:
        k -= 7

    i = 0

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        if cyclery >= 100:
            cyclery -= 3
            slow -= 2

    if keys[pygame.K_DOWN]:
        if cyclery <= 380:
            cyclery += 3
            slow += 2

    pygame.draw.rect(DISPLAYSURF, GREEN, (0, 100, 800, 50))
    pygame.draw.rect(DISPLAYSURF, STREET, (0, 150, 800, 300))
    while i <= 900:
        pygame.draw.rect(DISPLAYSURF, BLACK, (i, 300, 25, 5)).move(2,2)
        i = i + 30

    DISPLAYSURF.blit(redcarImg, (k, j))
    DISPLAYSURF.blit(cyclerImg, (cyclerx, cyclery))
    pygame.display.update()
    fpsClock.tick(FPS)

import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1000, 1000))

circle(screen, (255, 200, 255), (200, 200), 100)
rect(screen, (200, 70, 200), (170, 250, 50, 20))
circle(screen, (55, 0, 255), (170, 170), 20)
circle(screen, (55, 0, 255), (260, 170), 20)
circle(screen, (0, 0, 0), (170, 170), 10)
circle(screen, (0, 0, 0), (260, 170), 10)
polygon(screen, (0, 100, 0), [(100,100), (100,130),
                               (200,150), (100,100)])
polygon(screen, (0, 100, 0), [(290,100), (290,130),
                               (200,150), (290,100)])
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()



import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 600))
circle(screen, (255, 255, 0), (240, 240), 120)
circle(screen, (225, 69, 0), (192, 216), 30)
circle(screen, (225, 69, 0), (288, 216), 30)
circle(screen, (0, 0, 0), (288, 216),18)
circle(screen, (0, 0, 0), (192, 216), 18)
circle(screen, (0, 0, 0), (240, 240), 18)
polygon(screen, (0, 0, 0),[(150,180),(144,162),(234,174),(234,186)])
polygon(screen, (0, 0, 0),[(246,186),(246,174),(330,162),(330,180)])
polygon(screen, (0, 0, 0),[(192,300),(288,300),(288,312),(192,312)])

pygame.display.update()
face = pygame.time.Face()
finished = False

while not finished:
    face.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
            

pygame.quit()


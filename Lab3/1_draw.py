import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 600))
x=0
y=0
for j in range(5):
    for i in range(5):
        circle(screen, (255, 255, 0), (80+x, 80+y), 40)
        circle(screen, (225, 69, 0), (64+x, 72+y), 10)
        circle(screen, (225, 69, 0), (96+x, 72+y), 10)
        circle(screen, (0, 0, 0), (96+x, 72+y),6)
        circle(screen, (0, 0, 0), (64+x, 72+y), 6)
        if i % 2 == 0:
            if j % 2 ==0:
                circle(screen, (0, 0, 0), (80+x, 80+y), 6)
                polygon(screen, (0, 0, 0),[(50+x,60+y),(48+x,54+y),(78+x,58+y),(78+x,62+y)])
                polygon(screen, (0, 0, 0),[(82+x,62+y),(82+x,58+y),(110+x,54+y),(110+x,60+y)])
            else:
                polygon(screen, (0, 0, 0), [(70+x, 80+y),(90+x, 80+y),(80+x,90+y)])
                polygon(screen, (0, 0, 0),[(50+x,62+y),(48+x,58+y),(78+x,54+y),(78+x,60+y)])
                polygon(screen, (0, 0, 0),[(82+x,60+y),(82+x,54+y),(110+x,58+y),(110+x,62+y)])
        elif j % 2 ==1:
            circle(screen, (0, 0, 0), (80+x, 80+y), 6)
            polygon(screen, (0, 0, 0),[(50+x,60+y),(48+x,54+y),(78+x,58+y),(78+x,62+y)])
            polygon(screen, (0, 0, 0),[(82+x,62+y),(82+x,58+y),(110+x,54+y),(110+x,60+y)])
        else:
            polygon(screen, (0, 0, 0), [(70+x, 80+y),(90+x, 80+y),(80+x,90+y)])
            polygon(screen, (0, 0, 0),[(50+x,62+y),(48+x,58+y),(78+x,54+y),(78+x,60+y)])
            polygon(screen, (0, 0, 0),[(82+x,60+y),(82+x,54+y),(110+x,58+y),(110+x,62+y)])
        polygon(screen, (0, 0, 0),[(64+x,100+y),(96+x,100+y),(96+x,104+y),(64+x,104+y)])
        x = x + 160
    y = y + 100
    x = 0


pygame.display.update()
face = pygame.time.Clock()
finished = False

while not finished:
    face.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
            

pygame.quit()

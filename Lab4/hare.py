import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 600))

def draw_ear(surface, x, y, width, height, color):
    ''' Функция рисует ухо зайца.
    surface - oбъект pygame.Surface
    x, y - координаты левого верхнего угла изображения
    width, height - ширина и высота изображения
    color - цвет, заданный в формате, подходящем для pygame.Color
    '''
    ellipse(surface, color, (x, y, width, height))
    
def draw_eye(surface, x, y, width, height):
    ''' Функция рисует глаз зайца.
    surface - oбъект pygame.Surface
    x, y - координаты левого верхнего угла изображения
    width, height - ширина и высота изображения
    '''
    ellipse(surface, (0, 0, 0), (x, y, width, height))
    
def draw_head(surface, x, y, width, height, color):
    ''' Функция рисует голову зайца.
    surface - oбъект pygame.Surface
    x, y - координаты левого верхнего угла изображения
    width, height - ширина и высота изображения
    color - цвет, заданный в формате, подходящем для pygame.Color
    '''
    ellipse(surface, color, (x, y, width, height))
    draw_eye(surface, x + width // 16, y + height*5 // 16, width*3 // 8, height*3 // 8)
    draw_eye(surface, x + width*9 // 16, y + height*5 // 16, width*3 // 8, height*3 // 8)

             
def draw_body(surface, x, y, width, height, color):
    ''' Функция рисует тело зайца.
    surface - oбъект pygame.Surface
    x, y - координаты левого верхнего угла изображения
    width, height - ширина и высота изображения
    color - цвет, заданный в формате, подходящем для pygame.Color
    '''
    ellipse(surface, color, (x, y, width, height))

def draw_leg(surface, x, y, width, height, color):
    ''' Функция рисует ногу зайца.
    surface - oбъект pygame.Surface
    x, y - координаты левого верхнего угла изображения
    width, height - ширина и высота изображения
    color - цвет, заданный в формате, подходящем для pygame.Color
    '''
    ellipse(surface, color, (x, y, width, height))

def draw_hare(surface, x, y, width, height, color):
    ''' Функция рисует зайца.
    surface - oбъект pygame.Surface
    x, y - координаты левого верхнего угла изображения
    width, height - ширина и высота изображения
    color - цвет, заданный в формате, подходящем для pygame.Color
    '''
    draw_ear(surface, x + width // 6, y, width // 3, height*7 // 16, color)
    draw_ear(surface, x + width // 2, y, width // 3, height*7 // 16, color)
    draw_head(surface, x + width // 6, y + height*5 // 16, width*2 // 3, height // 4, color)
    draw_body(surface, x + width // 6, y + height*9 // 16, width*2 // 3, height*3 // 8, color)
    draw_leg(surface, x, y + height*15 // 16, width // 2, height // 16, color)
    draw_leg(surface, x + width // 2, y + height*15 // 16, width // 2, height // 16, color)
    

draw_hare(screen, 50, 50, 120, 320, (0, 255, 0))

pygame.display.update()
face = pygame.time.Face()
finished = False

while not finished:
    face.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
            

pygame.quit()


import pygame
from pygame.draw import *
from random import randint
import time
pygame.init()

FPS = 60
width = 1200
height = 500
screen = pygame.display.set_mode((width, height))

WHITE = (255, 255, 255)
PEACH = (255, 218, 125)
KHAKI = (240, 230, 140)
PINK = (255, 129, 203)
SALMON = (255, 160, 122)
LEMON = (255, 250, 205)
TAN = (210, 180, 140)
BLUE = (0, 0, 205)
NAVY = (0, 0, 128)
INDIGO = (75, 0, 130)
PURPLE = (128, 0, 128)
SKYBLUE = (0, 191, 255)
BLACK = (0, 0, 0)
COLORS = [PEACH, PINK, KHAKI, SALMON, LEMON, TAN]
FLOWERCOLORS = [BLUE, NAVY, INDIGO, PURPLE, SKYBLUE]

flowers = []
balls = []


def new_ball():
    '''Создает новый шарик.
    :param r:             радиус шарика
    :param x:             координата x центра шарика
    :param y:             координата y центра шарика
    :param vx:            скорость шарика по оси x
    :param vy:            скорость шарика по оси y
    :param spawn_time:    время появления шарика'''
    r = randint(20, 60)
    x = randint(r, width - r)
    y = randint(r, height - r)
    vx = randint(30, 100) / 100
    vy = randint(30, 100) / 100
    color = COLORS[randint(0, 5)]
    spawn_time = time.time()
    balls.append([x, y, r, color, vx, vy, spawn_time])


def draw_balls():
    '''Рисует шарики.'''
    for ball in balls:
        circle(screen, ball[3], (int(ball[0]), int(ball[1])), ball[2])

def move_balls():
    '''Двигает шарики.'''
    i = 0
    while i < len(balls):
        if time.time() - balls[i][6] > life_time:
            balls.pop(i)
        else:
            i += 1
    for ball in balls:
        x = ball[0]
        y = ball[1]
        r = ball[2]
        vx = ball[4]
        vy = ball[5]
        if (x + r + vx > width or x - r + vx < 0) :
            ball[4] = -ball[4]

        if (y + r + vy > height or y - r + vy < 0) :
            ball[5] = -ball[5]

        ball[0] += ball[4]
        ball[1] += ball[5]

def new_flower():
    '''Создает новый цветок.
    :param r:             1/5 радиуса цветка
    :param x:             координата x центра цветка
    :param y:             координата y центра цветка
    :param vx:            скорость цветка по оси x
    :param vy:            скорость цветка по оси y
    :param spawn_time:    время появления цветка'''
    r = randint(4, 20)
    x = randint(r, width - 5*r)
    y = randint(r, height - 5*r)
    vx = randint(0, 30) / 100
    vy = randint(0, 30) / 100
    color = FLOWERCOLORS[randint(0, 4)]
    spawn_time = time.time()
    flowers.append([x, y, r, color, vx, vy, spawn_time])


def draw_flowers():
    '''Рисует цветы.'''
    for flower in flowers:
        x = flower[0]
        y = flower[1]
        r = flower[2]
        polygon(screen, flower[3], [(x, y), (x - r, y + 5 * r), (x, y + 4 * r), (x + r, y + 5 * r)])
        polygon(screen, flower[3],
                [(x, y), (x + 3 * r, y + 4 * r), (x + 3 * r, y + 3 * r), (x + 4 * r, y + 3 * r)])
        polygon(screen, flower[3], [(x, y), (x + 5 * r, y + r), (x + 4 * r, y), (x + 5 * r, y - r)])
        polygon(screen, flower[3],
                [(x, y), (x + 4 * r, y - 3 * r), (x + 3 * r, y - 3 * r), (x + 3 * r, y - 4 * r)])
        polygon(screen, flower[3], [(x, y), (x + r, y - 5 * r), (x, y - 4 * r), (x - r, y - 5 * r)])
        polygon(screen, flower[3],
                [(x, y), (x - 3 * r, y + 4 * r), (x - 3 * r, y + 3 * r), (x - 4 * r, y + 3 * r)])
        polygon(screen, flower[3], [(x, y), (x - 5 * r, y + r), (x - 4 * r, y), (x - 5 * r, y - r)])
        polygon(screen, flower[3],
                [(x, y), (x - 4 * r, y - 3 * r), (x - 3 * r, y - 3 * r), (x - 3 * r, y - 4 * r)])

def move_flowers():
    '''Двигает цветы.'''
    i = 0
    while i < len(flowers):
        if time.time() - flowers[i][6] > life_time:
            flowers.pop(i)
        else:
            i += 1
    for flower in flowers:
        x = flower[0]
        y = flower[1]
        r = 5*flower[2]
        vx = flower[4]
        vy = flower[5]
        if (x + r + vx > width or x - r + vx < 0) :
            flower[4] = -flower[4]

        if (y + r + vy > height or y - r + vy < 0) :
            flower[5] = -flower[5]

        flower[0] += flower[4]
        flower[1] += flower[5]


def draw_score():
    '''Выводит на экран счет.'''
    f = pygame.font.Font(None, 36)
    text = f.render("Score: " + str(score), 0, WHITE)
    screen.blit(text, (0, 0))

pygame.display.update()
clock = pygame.time.Clock()
finished = False
last_ball_time = time.time()
last_flower_time = time.time()
score = 0
spawn_delta = 1
life_time = 5
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            i = len(balls) - 1
            while i > 0:
                x = balls[i][0]
                y = balls[i][1]
                r = balls[i][2]
                if (x - event.pos[0]) ** 2 + (y - event.pos[1]) ** 2 <= r ** 2:
                    score += 1
                    balls.pop(i)
                    break
                else:
                    i -= 1
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            i = len(flowers) - 1
            while i > 0:
                x = flowers[i][0]
                y = flowers[i][1]
                r = 5*flowers[i][2]
                if (x - event.pos[0]) ** 2 + (y - event.pos[1]) ** 2 <= r ** 2:
                    score += 5
                    flowers.pop(i)
                    break
                else:
                    i -= 1
    if (time.time() - last_ball_time > spawn_delta):
        new_ball()
        last_ball_time = time.time()
    if (time.time() - last_flower_time > spawn_delta):
        new_flower()
        last_flower_time = time.time()
    move_balls()
    move_flowers()
    screen.fill(BLACK)
    draw_balls()
    draw_flowers()
    draw_score()
    pygame.display.update()
print(score)
pygame.quit()
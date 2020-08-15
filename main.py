#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import numpy as np
from copy import deepcopy
from numba import njit
from random import randint


RESOLUTION = WIDTH, HEIGHT = 1600, 900
TILE = 5
W, H = WIDTH // TILE, HEIGHT // TILE
FPS = -1

pygame.init()
game_screen = pygame.display.set_mode(RESOLUTION)
clock = pygame.time.Clock()

next_field = np.array([[0 for i in range(W)] for j in range(H)])
current_field = np.array([[1 if not (i * j) % 22 else 0 for i in range(W)] for j in range(H)])

@njit(fastmath=True)
def check_cells(current_field, next_field):
    res = []
    for x in range(1, W - 1):
        for y in range(1, H - 1):
            count = 0
            for j in range(y - 1, y + 2):
                for i in range(x - 1, x + 2):
                    if current_field[j][i] == 1:
                        count += 1

            if current_field[y][x] == 1:
                count -= 1
                if count == 2 or count == 3:
                    next_field[y][x] = 1
                    res.append((x, y))
                else:
                    next_field[y][x] = 0
            else:
                if count == 3:
                    next_field[y][x] = 1
                    res.append((x, y))
                else:
                    next_field[y][x] = 0
    return next_field, res


while True:

    game_screen.fill(pygame.Color("black"))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    [pygame.draw.line(game_screen, pygame.Color('black'), (x, 0), (x, HEIGHT)) for x in range(0, WIDTH, TILE)]
    [pygame.draw.line(game_screen, pygame.Color('black'), (0, y), (WIDTH, y)) for y in range(0, HEIGHT, TILE)]
    
    # draw life
    next_field, res = check_cells(current_field, next_field)
    [pygame.draw.rect(game_screen, pygame.Color("darkorange"),
                      (x * TILE + 1, y * TILE + 1, TILE - 1, TILE - 1)) for x, y in res]

    current_field = deepcopy(next_field)

    # print(clock.get_fps())
    pygame.display.flip()
    clock.tick(FPS)
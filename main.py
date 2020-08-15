#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
from copy import deepcopy
from numba import jit
from random import randint


RESOLUTION = WIDTH, HEIGHT = 1600, 900
TILE = 5
W, H = WIDTH // TILE, HEIGHT // TILE
FPS = -1

pygame.init()
game_screen = pygame.display.set_mode(RESOLUTION)
clock = pygame.time.Clock()

while True:

    game_screen.fill(pygame.Color('black'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # print(clock.get_fps())
    pygame.display.flip()
    clock.tick(FPS)
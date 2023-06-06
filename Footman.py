import random

import pygame

from Enemy import *
from CONST import *


class Footman(Enemy):
    def __init__(self, pos):
        self.pos = pos * BLOCK_SIZE
        self.actual_tile = 0
        self.HP = FOOTMAN_HP
        self.frame = random.randint(0, 2)
        self.frame_change = pygame.time.get_ticks()

    def update(self, dt, path):
        dest = path[self.actual_tile + 1] * BLOCK_SIZE
        if self.pos.distance_to(dest) < MOVE_PRECISION:
            self.actual_tile += 1
            self.actual_tile = min(self.actual_tile, len(path) - 2)
        if (pygame.time.get_ticks() - self.frame_change) / 1000 > ANIMATION_TIME:
            self.frame_change = pygame.time.get_ticks()
            self.frame += 1
            self.frame %= 3
        self.pos.move_towards_ip(dest, FOOTMAN_SPEED * dt)

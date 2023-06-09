import random

import pygame

from Enemy import *
from CONST import *


class Knight(Enemy):
    '''
    Klasa Knight reprezentuje jednostkę przeciwnika, która ma dużo życia, ale wolno się porusza.
    Klasa posiada pola:
        - pos: pygame.Vector2
        - actual_tile: int
        - HP: float
        - frame: int
        - frame_change: float
    Metody:
        - __init__: void
        - update: void
    '''
    def __init__(self, pos: tuple):
        '''
        Konstruktor klasy Knight
        :param pos: 2-elementowa krotka opisująca pozycję na ścieżce.
        :type pos: tuple
        :return: void
        '''
        self.pos: pygame.Vector2 = pygame.Vector2(pos.x * BLOCK_SIZE, pos.y * BLOCK_SIZE - 5)
        self.actual_tile: int = 0
        self.HP: float = KNIGHT_HP
        self.frame: int = random.randint(0, 3)
        self.frame_change: float = pygame.time.get_ticks()

    def update(self, dt: float, path: list):
        '''
        Metoda akutalizująca pozycję i klatkę animacji obiektu klasy Knight.
        :param dt: float
        :param path: list
        :return: void
        '''
        dest: pygame.Vector2 = pygame.Vector2(path[self.actual_tile + 1][0] * BLOCK_SIZE, path[self.actual_tile + 1][1] * BLOCK_SIZE - 5)
        if self.pos.distance_to(dest) < MOVE_PRECISION:
            self.actual_tile += 1
            self.actual_tile = min(self.actual_tile, len(path) - 2)
        if (pygame.time.get_ticks() - self.frame_change) / 1000 > KNIGHT_ANIMATION_TIME:
            self.frame_change = pygame.time.get_ticks()
            self.frame += 1
            self.frame %= 4
        self.pos.move_towards_ip(dest, KNIGHT_SPEED * dt)
import random

import pygame

from Enemy import *
from CONST import *


class Wolf(Enemy):
    """Klasa, dziedzicząca po abstrakcyjnej klasie Enemy, reprezentuje wilka, \
    który jest przeciwnikiem i której instancje są tworzone podczas trwania gry.

    Attributes:
        pos (pygame.Vector2): Para koordynatów reprezentująca pozycję przeciwnika.

        actual_tile (int): indeks listy reprezentującej ścieżkę, \
        który opisuje obecną pozycję przeciwnika na ścieżce.

        HP (float): Ilość punktów życia przeciwnika.

        frame (int): Numer klatki animacji, która powinna zostać narysowana.

        frame_change (float): Czas jaki minął od zmiany klatki animacji.
    """
    def __init__(self, pos):
        """Inicjowanie przeciwnika.

        Args:
            pos (pygame.Vector2): Para koordynatów opisująca pozycję przeciwnika.
        Returns:
            void
        """
        self.pos: pygame.Vector2 = pygame.Vector2(pos.x * BLOCK_SIZE, pos.y * BLOCK_SIZE + 2)
        self.actual_tile: int = 0
        self.HP: float = WOLF_HP
        self.frame: int = random.randint(0, 3)
        self.frame_change: float = pygame.time.get_ticks()

    def update(self, dt, path):
        """Zaktualizowanie obiektu przeciwnika.

        Args:
            dt (float): Skalar, przez który przemnażane są zmienne, \
            aby zadbać o jednolite działanie programu, \
            niezależnie od prędkości jego działania.

            path (list): Lista par koordynatów reprezentująca ścieżkę, \
            po której porusza się przeciwnik.
        Returns:
            void
        """
        dest: pygame.Vector2 = pygame.Vector2(path[self.actual_tile + 1][0] * BLOCK_SIZE, path[self.actual_tile + 1][1] * BLOCK_SIZE + 2)
        if self.pos.distance_to(dest) < MOVE_PRECISION:
            self.actual_tile += 1
            self.actual_tile = min(self.actual_tile, len(path) - 2)
        if (pygame.time.get_ticks() - self.frame_change) / 1000 > WOLF_ANIMATION_TIME:
            self.frame_change = pygame.time.get_ticks()
            self.frame += 1
            self.frame %= 5
        self.pos.move_towards_ip(dest, WOLF_SPEED * dt)
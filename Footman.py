# -----------------------------------------------------------------------------
# Marcin Banak
# Zadanie końcowe na przedmiot "Programowanie obiektowe"
# Gra "Tower defense"
# Data utworzenia: 14.06.2023
# Wersja 1.0.0
# -----------------------------------------------------------------------------

import random
import pygame

from Enemy import *
from CONST import *


class Footman(Enemy):
    """Klasa, dziedzicząca po abstrakcyjnej klasie Enemy, reprezentuje żołnierza, \
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
        self.pos = pos * BLOCK_SIZE
        self.actual_tile = 0
        self.HP = FOOTMAN_HP
        self.frame = random.randint(0, 2)
        self.frame_change = pygame.time.get_ticks()

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
        dest = path[self.actual_tile + 1] * BLOCK_SIZE
        if self.pos.distance_to(dest) < MOVE_PRECISION:
            self.actual_tile += 1
            self.actual_tile = min(self.actual_tile, len(path) - 2)
        if (pygame.time.get_ticks() - self.frame_change) / 1000 > FOOTMAN_ANIMATION_TIME:
            self.frame_change = pygame.time.get_ticks()
            self.frame += 1
            self.frame %= 3
        self.pos.move_towards_ip(dest, FOOTMAN_SPEED * dt)

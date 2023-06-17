# -----------------------------------------------------------------------------
# Marcin Banak
# Zadanie końcowe na przedmiot "Programowanie obiektowe"
# Gra "Tower defense"
# Data utworzenia: 14.06.2023
# Wersja 1.0.0
# -----------------------------------------------------------------------------

import pygame

from Building import *
from CONST import *


class ArtilleryTower(Building):
    """Klasa, dziedzicząca po abstrakcyjnej klasie Building, reprezentuje wieżę artyleryjską, \
    której instancje gracz może tworzyć podczas trwania gry.

    Attributes:
        pos (pygame.Vector2): Para koordynatów reprezentująca pozycję wieży.

        last_shot (int): Zmienna śledząca ilość czasu jaka minęła od ostatniego  \
        wystrzelenia pocisku przez wieżę.

        shoot (bool): Wartość logiczna określająca, czy wieża wykonała strzał, \
        bazowo ustawiona na False.

        target (Enemy): Przeciwnik, który jest celem wieży bazowo ustawiony na None.
    """
    def __init__(self, pos):
        """Inicjowanie wieży.

        Args:
            pos (pygame.Vector2): Para koordynatów opisująca pozycję wieży.
        Returns:
            void
        """
        self.pos = pos
        self.center = pygame.Vector2(pos.x + TOWER_SIZE.x // 2, pos.y + TOWER_SIZE.y // 2)
        self.last_shot = pygame.time.get_ticks()
        self.shoot = False
        self.target = None

    def update(self, enemies):
        """Zaktualizowanie obiektu wieży

        Args:
            enemies (list): Lista przeciwników, w której znajdujemy przeciwnika, \
            do którego powinna strzelać wieża.
        Returns:
            void
        """
        if self.shoot:
            self.shoot = False
        for enemy in enemies:
            if (pygame.time.get_ticks() - self.last_shot) / 1000 > ARCHER_TOWER_SPEED:
                if self.pos.distance_to(enemy.pos) < ARCHER_TOWER_RANGE:
                    self.last_shot = pygame.time.get_ticks()
                    self.target = enemy
                    self.shoot = True
                    break
                else:
                    self.Target = None



# -----------------------------------------------------------------------------
# Marcin Banak
# Zadanie końcowe na przedmiot "Programowanie obiektowe"
# Gra "Tower defense"
# Data utworzenia: 14.06.2023
# Wersja 1.0.0
# -----------------------------------------------------------------------------

import pygame
from CONST import *


class Tile:
    """Klasa reprezentująca pole wieży.

    Attributes:
        pos (pygame.Vector2): Para koordynatów opisująca położenie pola wieży.
        rect (pygame.Rect): Obiekt prostokątu \
        służący do wykrywania kolizji myszki z polem wieży.
        state (string): Zmienna opisująca stan pola wieży.
        clicked (bool): Wartość logiczna opisująca, czy pole wieży zostało wybrane.
    """
    def __init__(self, pos):
        """Inicjowanie pola wieży.

        Args:
            pos (pygame.Vector2): Para koordynatów opisująca pozycję pola wieży.
            size (pygame.Vector2): Para opisująca wymiary pola wieży.
        Returns:
            void
        """
        self.pos = pos * BLOCK_SIZE
        self.rect = pygame.Rect(0, 0, TILE_SIZE.x, TILE_SIZE.y)
        self.rect.center = pygame.Vector2(pos.x * BLOCK_SIZE + TILE_SIZE.x // 2, pos.y * BLOCK_SIZE + TILE_SIZE.y // 2)
        self.state = "normal"
        self.clicked = False
        self.make_buttons = False

    def update(self, mouse):
        """Zaktualizowanie obiektu pola wieży.

        Args:
            mouse: (Mouse): Obiekt myszki służący do określenia stanu pola wieży.
        Returns:
            void
        """
        if self.make_buttons:
            self.make_buttons = False
        if self.rect.colliderect(mouse.rect):
            if mouse.click_switch:
                self.state = "touched"
            else:
                self.state = "clicked"
            if mouse.click and not self.clicked:
                self.state = "clicked"
                self.clicked = True
                self.make_buttons = True
        elif mouse.click and self.clicked:
            self.state = "normal"
            self.clicked = False
        else:
            self.state = "normal"
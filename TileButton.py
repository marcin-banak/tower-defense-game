# -----------------------------------------------------------------------------
# Marcin Banak
# Zadanie końcowe na przedmiot "Programowanie obiektowe"
# Gra "Tower defense"
# Data utworzenia: 14.06.2023
# Wersja 1.0.0
# -----------------------------------------------------------------------------

import pygame
from CONST import *


class TileButton:
    """Klasa reprezentująca przycisk wyboru typu wieży, \
    która ma zostać zbudowana na danym polu.

    Attributes:
        pos (pygame.Vector2): Para koordynatów opisująca położenie przycisku.
        rect (pygame.Rect): Obiekt prostokątu \
        służący do wykrywania kolizji myszki z przyciskiem.
        state (string): Zmienna opisująca stan przycisku.
        clicked (bool): Wartość logiczna opisująca, czy przycisk został wciśnięty.
    """
    def __init__(self, pos, size, type, tile):
        """Inicjowanie przycisku.

        Args:
            pos (pygame.Vector2): Para koordynatów opisująca pozycję przycisku.

            size (pygame.Vector2): Para opisująca wymiary przycisku.

            type (string): Napis determinujący jaki typ wieży powinien zostać stworzony \
            po wciśnięciu przycisku.

            tile (Tile): Pole wieży, do którego przypisane są przyciski wyboru typu wieży.
        Returns:
            void
        """
        self.pos = pos
        self.rect = pygame.Rect(0, 0, size.x, size.y)
        self.rect.center = pygame.Vector2(pos.x + size.x // 2, pos.y + size.y // 2)
        self.type = type
        self.tile = tile
        self.state = "normal"
        self.clicked = False
        self.sound_to_play = None

    def update(self, mouse):
        """Zaktualizowanie obiektu przycisku.

        Args:
            mouse: (Mouse): Obiekt myszki służący do określenia stanu przycisku.
        Returns:
            void
        """
        if self.rect.colliderect(mouse.rect):
            if mouse.click_switch:
                if self.state == "normal":
                    self.sound_to_play = "touch"
                self.state = "touched"
            else:
                self.state = "clicked"
            if mouse.click and not self.clicked:
                self.state = "clicked"
                self.clicked = True
                self.sound_to_play = "click"
        elif mouse.click and self.clicked:
            self.state = "normal"
            self.clicked = False
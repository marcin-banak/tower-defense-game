# -----------------------------------------------------------------------------
# Marcin Banak
# Zadanie końcowe na przedmiot "Programowanie obiektowe"
# Gra "Tower defense"
# Data utworzenia: 14.06.2023
# Wersja 1.0.0
# -----------------------------------------------------------------------------

import pygame
from CONST import *

class Mouse:
    """Klasa myszki, dzięki której program może obsługiwać związane z nią zdarzenia.

    Attributes:
        rect (pygame.Rect): Prostokąt służący do wykrywania \
        kolizji myszki z innymi obiektami.

        click (bool): Wartość logiczna mówiąca, czy myszka jest kliknięta.

        click_switch (bool): Wartość logiczna dbająca o to by wartość zmiennej click \
        została ustawiona na False przy puszczeniu przycisku myszy.
    """
    def __init__(self):
        """Inicjowanie myszki.

        Returns:
            void
        """
        self.rect = pygame.Rect(0,0,1,1)
        self.click = False
        self.click_switch = True

    def update(self, screen_size):
        """Zaktualizowanie obiektu myszy.

        Args:
            screen_size (pygame.Vector2): Para liczb określająca rozdzielczość ekranu, \
            używana do przeskalowania pozycji myszki do wymiarów płaszczyzny, \
            na której rysowany jest program.
        Returns:
            void
        """
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0] * DRAW_SCREEN_SIZE[0] // screen_size[0]
        self.rect.y = pos[1] * DRAW_SCREEN_SIZE[1] // screen_size[1]

        # button
        if pygame.mouse.get_pressed()[0]:
            if self.click_switch:
                self.click = True
                self.click_switch = False
            else:
                self.click = False
        else:
            self.click_switch = True
            self.click = False

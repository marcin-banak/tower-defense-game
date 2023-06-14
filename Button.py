import pygame
from CONST import *


class Button:
    """Klasa reprezentująca przycisk w menu.

    Attributes:
        pos (pygame.Vector2): Para koordynatów opisująca położenie przycisku.
        rect (pygame.Rect): Obiekt prostokątu \
        służący do wykrywania kolizji myszki z przyciskiem.
        state (string): Zmienna opisująca stan przycisku.
        clicked (bool): Wartość logiczna opisująca, czy przycisk został wciśnięty.
    """
    def __init__(self, pos, size):
        """Inicjowanie przycisku.

        Args:
            pos (pygame.Vector2): Para koordynatów opisująca pozycję przycisku.
            size (pygame.Vector2): Para opisująca wymiary przycisku.
        Returns:
            void
        """
        self.pos = pos
        self.rect = pygame.Rect(0, 0, size.x, size.y)
        self.rect.center = pygame.Vector2(pos.x + size.x // 2, pos.y + size.y // 2)
        self.state = "normal"
        self.clicked = False

    def update(self, mouse):
        """Zaktualizowanie obiektu przycisku.

        Args:
            mouse: (Mouse): Obiekt myszki służący do określenia stanu przycisku.
        Returns:
            void
        """
        if self.rect.colliderect(mouse.rect):
            if mouse.click_switch:
                self.state = "touched"
            else:
                self.state = "clicked"
            if mouse.click and not self.clicked:
                self.state = "clicked"
                self.clicked = True
        elif mouse.click and self.clicked:
            self.state = "normal"
            self.clicked = False
# -----------------------------------------------------------------------------
# Marcin Banak
# Zadanie końcowe na przedmiot "Programowanie obiektowe"
# Gra "Tower defense"
# Data utworzenia: 14.06.2023
# Wersja 1.0.0
# -----------------------------------------------------------------------------

from Projectile import *
from CONST import *


class Arrow(Projectile):
    """Klasa, dziedzicząca po abstrakcyjnej klasie Projectile, \
    reprezentuje pocisk strzały, której instancje są tworzone podczas trwania gry.

    Attributes:
        pos (pygame.Vector2): Para koordynatów reprezentująca pozycję pocisku.

        target (Enemy): Obiekt przeciwnika, który jest celem pocisku.

        hit (bool): Zmienna mówiąca czy pocisk trafił swój cel. \
        W momencie trafienia, pocisk zostaje zwolniony z pamięci.
    """
    def __init__(self, pos, target):
        """Inicjowanie pocisku.

        Args:
            pos (pygame.Vector2): pozycja pocisku.
            target (Enemy): cel pocisku.
        Returns:
            void
        """
        self.pos = pos
        self.target = target
        self.hit = False

    def update(self, dt):
        """Zaktualizowanie obiektu pocisku.

        Args:
            dt (float): Skalar, przez który przemnażane są zmienne, \
            aby zadbać o jednolite działanie programu, \
            niezależnie od prędkości jego działania.
        Returns:
            void
        """
        dest = self.target.pos
        self.pos.move_towards_ip(dest, ARROW_SPEED * dt)
        if self.pos.distance_to(dest) < MOVE_PRECISION:
            self.target.HP -= ARROW_DAMAGE
            self.hit = True
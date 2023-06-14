from Projectile import *
from CONST import *


class Beam(Projectile):
    """Klasa, dziedzicząca po abstrakcyjnej klasie Projectile, \
    reprezentuje promień magiczny, którego instancje są tworzone podczas trwania gry.

    Attributes:
        pos (pygame.Vector2): Para koordynatów reprezentująca pozycję pocisku.

        target (Enemy): Obiekt przeciwnika, który jest celem pocisku.

        hit (bool): Zmienna mówiąca czy pocisk trafił swój cel. \
        W momencie trafienia, pocisk zostaje zwolniony z pamięci.
    """
    def __init__(self, pos, target):
        """Inicjowanie wieży.

        Args:
            pos (pygame.Vector2): Para opisująca pozycję wieży.
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
        self.pos.move_towards_ip(dest, BEAM_SPEED * dt)
        if self.pos.distance_to(dest) < MOVE_PRECISION:
            self.target.HP -= BEAM_DAMAGE
            self.hit = True
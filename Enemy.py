# -----------------------------------------------------------------------------
# Marcin Banak
# Zadanie końcowe na przedmiot "Programowanie obiektowe"
# Gra "Tower defense"
# Data utworzenia: 14.06.2023
# Wersja 1.0.0
# -----------------------------------------------------------------------------

from abc import ABC, abstractmethod


class Enemy(ABC):
    """Abstrakcyjna klasa, po której dziedziczą wszystkie klasy przeciwników.
    """
    @abstractmethod
    def update(self, dt):
        pass
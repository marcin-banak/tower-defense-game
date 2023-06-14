from abc import ABC, abstractmethod


class Projectile(ABC):
    """Abstrakcyjna klasa, po której dziedziczą wszystkie klasy pocisków.
    """
    @abstractmethod
    def update(self):
        pass
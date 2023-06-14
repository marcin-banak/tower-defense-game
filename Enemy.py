from abc import ABC, abstractmethod


class Enemy(ABC):
    """Abstrakcyjna klasa, po której dziedziczą wszystkie klasy przeciwników.
    """
    @abstractmethod
    def update(self, dt):
        pass
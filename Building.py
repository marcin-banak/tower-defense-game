from abc import ABC, abstractmethod


class Building(ABC):
    """Abstrakcyjna klasa, po której dziedziczą wszystkie klasy wież.
    """
    @abstractmethod
    def update(self):
        pass

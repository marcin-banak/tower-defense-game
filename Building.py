from abc import ABC, abstractmethod


class Building(ABC):
    @abstractmethod
    def update(self):
        pass

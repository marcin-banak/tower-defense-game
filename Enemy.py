from abc import ABC, abstractmethod


class Enemy(ABC):
    @abstractmethod
    def update(self, dt):
        pass
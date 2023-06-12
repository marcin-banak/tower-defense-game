from Building import *


class CannonTower(Building):
    def __init__(self, pos):
        self.pos = pos
        self.range = 32
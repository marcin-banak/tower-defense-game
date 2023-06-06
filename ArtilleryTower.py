import pygame

from Building import *
from CONST import *


class ArtilleryTower(Building):
    def __init__(self, pos):
        self.pos = pos
        self.center = pygame.Vector2(pos.x + TOWER_SIZE.x // 2, pos.y + TOWER_SIZE.y // 2)
        self.last_shot = pygame.time.get_ticks()
        self.shoot = False
        self.target = None

    def update(self, enemies):
        if self.shoot:
            self.shoot = False
        for enemy in enemies:
            if (pygame.time.get_ticks() - self.last_shot) / 1000 > ARTILLERY_TOWER_SPEED \
                    and self.pos.distance_to(enemy.pos) < ARTILLERY_TOWER_RANGE:
                self.last_shot = pygame.time.get_ticks()
                self.target = enemy
                self.shoot = True
                break



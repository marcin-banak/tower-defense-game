from CONST import *


class Bomb:
    def __init__(self, pos, target):
        self.pos = pos
        self.target = target
        self.hit = False

    def update(self, dt, enemies):
        dest = self.target.pos
        self.pos.move_towards_ip(dest, BOMB_SPEED * dt)
        if self.pos.distance_to(dest) < MOVE_PRECISION:
            for enemy in enemies:
                dist_to_enemy = self.pos.distance_to(enemy.pos)
                if dist_to_enemy <= BOMB_SPLASH_AREA:
                    enemy.HP -= BOMB_DAMAGE * dist_to_enemy / BOMB_SPLASH_AREA
            self.hit = True
from CONST import *


class Arrow:
    def __init__(self, pos, target):
        self.pos = pos
        self.target = target
        self.hit = False

    def update(self, dt):
        dest = self.target.pos
        self.pos.move_towards_ip(dest, ARROW_SPEED * dt)
        if self.pos.distance_to(dest) < MOVE_PRECISION:
            self.target.HP -= ARROW_DAMAGE
            self.hit = True
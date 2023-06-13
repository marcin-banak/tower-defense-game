from CONST import *


class Beam:
    def __init__(self, pos, target):
        self.pos = pos
        self.target = target
        self.hit = False

    def update(self, dt):
        dest = self.target.pos
        self.pos.move_towards_ip(dest, BEAM_SPEED * dt)
        if self.pos.distance_to(dest) < MOVE_PRECISION:
            self.target.HP -= BEAM_DAMAGE
            self.hit = True
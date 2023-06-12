import pygame
from CONST import *


class TileButton:
    def __init__(self, pos, size, type, tile):
        self.pos = pos
        self.rect = pygame.Rect(0, 0, size.x, size.y)
        self.rect.center = pygame.Vector2(pos.x + size.x // 2, pos.y + size.y // 2)
        self.type = type
        self.tile = tile
        self.state = "normal"
        self.clicked = False
        self.sound_to_play = None

    def update(self, mouse):
        if self.rect.colliderect(mouse.rect):
            if mouse.click_switch:
                if self.state == "normal":
                    self.sound_to_play = "touch"
                self.state = "touched"
            else:
                self.state = "clicked"
            if mouse.click and not self.clicked:
                self.state = "clicked"
                self.clicked = True
                self.sound_to_play = "click"
        elif mouse.click and self.clicked:
            self.state = "normal"
            self.clicked = False
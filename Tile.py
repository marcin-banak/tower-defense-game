import pygame
from CONST import *


class Tile:
    def __init__(self, pos):
        self.pos = pos * BLOCK_SIZE
        self.rect = pygame.Rect(0, 0, TILE_SIZE.x, TILE_SIZE.y)
        self.rect.center = pygame.Vector2(pos.x * BLOCK_SIZE + TILE_SIZE.x // 2, pos.y * BLOCK_SIZE + TILE_SIZE.y // 2)
        self.state = "normal"
        self.clicked = False
        self.make_buttons = False
        self.sound_to_play = None

    def update(self, mouse):
        if self.make_buttons:
            self.make_buttons = False
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
                self.make_buttons = True
        elif mouse.click and self.clicked:
            self.state = "normal"
            self.clicked = False
        else:
            self.state = "normal"
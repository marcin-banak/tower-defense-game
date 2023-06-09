import pygame

WIDTH, HEIGHT = 1024, 576
BLOCK_SIZE = 10
SCREEN_SIZE = pygame.Vector2(WIDTH, HEIGHT)
DRAW_SCREEN_SIZE = pygame.Vector2(320, 180)
TILE_SIZE = pygame.Vector2(20, 20)
FPS = 60
MOVE_PRECISION = 3
BASE_PRECISION = 7

FOOTMAN_HP = 120
FOOTMAN_SPEED = 0.2
FOOTMAN_BASE_DAMAGE = 1
FOOTMAN_ANIMATION_TIME = 0.3

KNIGHT_HP = 300
KNIGHT_SPEED = 0.07
KNIGHT_BASE_DAMAGE = 3
KNIGHT_ANIMATION_TIME = 0.2

WOLF_HP = 80
WOLF_SPEED = 0.3
WOLF_BASE_DAMAGE = 1
WOLF_ANIMATION_TIME = 0.2

TOWER_SIZE = pygame.Vector2(20, 40)

ARCHER_TOWER_RANGE = 70
ARCHER_TOWER_SPEED = 1
ARROW_SPEED = 1
ARROW_DAMAGE = 12

ARTILLERY_TOWER_RANGE = 50
ARTILLERY_TOWER_SPEED = 2.4
BOMB_SPEED = 0.9
BOMB_DAMAGE = 27
BOMB_SPLASH_AREA = 15


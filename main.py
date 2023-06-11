import time
import os
import random

import pygame
from pygame import *
from CONST import *
from Footman import *
from Knight import *
from Wolf import *
from ArcherTower import *
from Arrow import *
from ArtilleryTower import *
from Bomb import *
from mouse import *
from Tile import *
from TileButton import *
from Button import *


class Main:
    def __init__(self):
        # inicjalizacja zasobów modułu pygame.
        init()
        self.screen = display.set_mode(SCREEN_SIZE)
        self.draw_screen = pygame.Surface(DRAW_SCREEN_SIZE)
        self.font = pygame.font.Font("font.ttf", 14)
        display.set_caption("Tower defense")

        self.map = []
        self.map = self.load_map()
        self.textures = {}
        self.load_textures()
        self.mouse = Mouse()
        self.is_running = True
        self.clock = time.Clock()
        self.dt = 1

        self.path = []
        self.enemies = []
        self.tiles = []
        self.tile_buttons = []
        self.towers = []
        self.projectiles = []
        self.enemies_power = None
        self.base_HP = None

        self.buttons = []
        self.init_menu()

        while self.is_running:
            self.check_events()
            self.scene()
            self.display_update()
        quit()

    def check_events(self):
        self.mouse.update(SCREEN_SIZE)
        for e in event.get():
            if e.type == QUIT:
                self.is_running = False

    def display_update(self):
        self.dt = self.clock.tick(FPS) * 60 / 1000
        self.screen.blit(pygame.transform.scale(self.draw_screen, SCREEN_SIZE), (0, 0))
        display.update()

    def init_menu(self):
        self.buttons = self.init_buttons()
        self.scene = self.menu

    def menu(self):
        self.update_buttons()
        self.draw_menu()

    def draw_menu(self):
        self.draw_screen.fill((0, 0, 0))
        for button in self.buttons:
            self.draw_screen.blit(self.textures["startButton"], button.pos)

    def init_buttons(self):
        buttons = []
        buttons.append(Button(pygame.Vector2(115, 75), pygame.Vector2(90, 30)))
        return buttons

    def update_buttons(self):
        for button in self.buttons:
            button.update(self.mouse)
            if button.clicked:
                self.init_game()

    def init_game(self):
        self.path = self.get_path()
        self.enemies = self.init_enemies()
        self.tiles = self.init_tiles()
        self.base_HP = 20
        self.scene = self.game

    def game(self):
        self.update_enemies()
        self.update_tiles()
        self.update_towers()
        self.update_projectiles()

        if self.base_HP <= 0:
            self.init_menu()
            self.scene = self.menu
        self.draw_game()

    def draw_game(self):
        self.draw_screen.blit(self.textures["map"], (0, 0))
        for enemy in self.enemies:
            if isinstance(enemy, Footman):
                self.draw_screen.blit(self.textures["footman" + str(enemy.frame)], enemy.pos)
                if enemy.HP != FOOTMAN_HP:
                    pygame.draw.line(self.draw_screen, pygame.Color(0, 0, 0),
                                     pygame.Vector2(enemy.pos.x + 2, enemy.pos.y + 12),
                                     pygame.Vector2(enemy.pos.x + 8, enemy.pos.y + 12), 1)
                    pygame.draw.line(self.draw_screen, pygame.Color(255, 0, 0),
                                     pygame.Vector2(enemy.pos.x + 2, enemy.pos.y + 12),
                                     pygame.Vector2(enemy.pos.x + 8 * enemy.HP // FOOTMAN_HP, enemy.pos.y + 12), 1)
            elif isinstance(enemy, Knight):
                self.draw_screen.blit(self.textures["knight" + str(enemy.frame)], enemy.pos)
                if enemy.HP != KNIGHT_HP:
                    pygame.draw.line(self.draw_screen, pygame.Color(0, 0, 0),
                                     pygame.Vector2(enemy.pos.x + 2, enemy.pos.y + 17),
                                     pygame.Vector2(enemy.pos.x + 8, enemy.pos.y + 17), 1)
                    pygame.draw.line(self.draw_screen, pygame.Color(255, 0, 0),
                                     pygame.Vector2(enemy.pos.x + 2, enemy.pos.y + 17),
                                     pygame.Vector2(enemy.pos.x + 8 * enemy.HP // KNIGHT_HP, enemy.pos.y + 17), 1)
            else:
                self.draw_screen.blit(self.textures["wolf" + str(enemy.frame)], enemy.pos)
                if enemy.HP != WOLF_HP:
                    pygame.draw.line(self.draw_screen, pygame.Color(0, 0, 0),
                                     pygame.Vector2(enemy.pos.x + 2, enemy.pos.y + 10),
                                     pygame.Vector2(enemy.pos.x + 8, enemy.pos.y + 10), 1)
                    pygame.draw.line(self.draw_screen, pygame.Color(255, 0, 0),
                                     pygame.Vector2(enemy.pos.x + 2, enemy.pos.y + 10),
                                     pygame.Vector2(enemy.pos.x + 8 * enemy.HP // WOLF_HP, enemy.pos.y + 10), 1)
        for tile in self.tiles:
            if tile.state == "touched":
                self.draw_screen.blit(self.textures["tileLight"], tile.pos)
            if tile.clicked:
                self.draw_screen.blit(self.textures["frame"], pygame.Vector2(tile.pos.x - 10, tile.pos.y + 7))
                self.draw_screen.blit(self.textures["arrow"], pygame.Vector2(tile.pos.x - 10, tile.pos.y + 7))
                self.draw_screen.blit(self.textures["frame"], pygame.Vector2(tile.pos.x + 6, tile.pos.y - 10))
                self.draw_screen.blit(self.textures["beam"], pygame.Vector2(tile.pos.x + 6, tile.pos.y - 10))
                self.draw_screen.blit(self.textures["frame"], pygame.Vector2(tile.pos.x + 22, tile.pos.y + 7))
                self.draw_screen.blit(self.textures["bomb"], pygame.Vector2(tile.pos.x + 22, tile.pos.y + 7))
        for tower in self.towers:
            if isinstance(tower, ArcherTower):
                self.draw_screen.blit(self.textures["archer"], tower.pos)
            elif isinstance(tower, ArtilleryTower):
                self.draw_screen.blit(self.textures["artillery"], tower.pos)
        for projectile in self.projectiles:
            if isinstance(projectile, Arrow):
                self.draw_screen.blit(self.textures["arrow"], projectile.pos)
            else:
                self.draw_screen.blit(self.textures["bomb"], projectile.pos)
        self.draw_screen.blit(self.textures["statusBar"], pygame.Vector2(0, 0))
        self.draw_screen.blit(self.font.render(str(self.base_HP), True, pygame.Color(255, 255, 255)), pygame.Vector2(14, 2))

    def init_enemies(self):
        enemies = []
        enemies.append(Knight(self.path[0]))
        for i in range(5):
            enemies.append(Footman(pygame.Vector2((self.path[0].x + i + 1), self.path[0].y)))
        enemies.append(Wolf(self.path[0]))
        self.enemies_power = WOLF_POWER + 5 * FOOTMAN_POWER + KNIGHT_POWER
        return enemies

    def add_enemies(self):
        power = ENEMIES_MAX_POWER - random.randint(0, ENEMIES_POWER_INTERVAL)
        enemies = ["wolf", 'footman', 'knight']
        weights = [ENEMIES_SUM_POWER / WOLF_POWER, ENEMIES_SUM_POWER / FOOTMAN_POWER, ENEMIES_SUM_POWER / KNIGHT_POWER]
        i = 0
        while self.enemies_power < power:
            choice = random.choices(enemies, weights)
            if choice[0] == "wolf":
                self.enemies_power += WOLF_POWER
                self.enemies.append(Wolf(pygame.Vector2((self.path[0].x + i), self.path[0].y)))
            elif choice[0] == "footman":
                self.enemies_power += FOOTMAN_POWER
                self.enemies.append(Footman(pygame.Vector2((self.path[0].x + i), self.path[0].y)))
            else:
                self.enemies_power += KNIGHT_POWER
                self.enemies.append(Knight(pygame.Vector2((self.path[0].x + i), self.path[0].y)))
            i += 1

    def update_enemies(self):
        for enemy in self.enemies:
            enemy.update(self.dt, self.path)
            if enemy.pos.distance_to((self.path[len(self.path) - 2]) * BLOCK_SIZE) < BASE_PRECISION:
                if isinstance(enemy, Footman):
                    self.base_HP -= FOOTMAN_BASE_DAMAGE
                    self.enemies_power -= FOOTMAN_POWER
                elif isinstance(enemy, Knight):
                    self.base_HP -= KNIGHT_BASE_DAMAGE
                    self.enemies_power -= KNIGHT_POWER
                else:
                    self.base_HP -= WOLF_BASE_DAMAGE
                    self.enemies_power -= WOLF_POWER
                self.enemies.remove(enemy)
            elif enemy.HP <= 0:
                if isinstance(enemy, Footman):
                    self.enemies_power -= FOOTMAN_POWER
                elif isinstance(enemy, Knight):
                    self.enemies_power -= KNIGHT_POWER
                else:
                    self.enemies_power -= WOLF_POWER
                self.enemies.remove(enemy)
        if self.enemies_power <= ENEMIES_MIN_POWER:
            self.add_enemies()
        sorted(self.enemies, key = lambda enemy: (enemy.actual_tile))

    def init_tiles(self):
        tiles = []
        for y in range(int(DRAW_SCREEN_SIZE.y // BLOCK_SIZE)):
            for x in range(int(DRAW_SCREEN_SIZE.x // BLOCK_SIZE)):
                if self.map[y][x] == '*':
                    tiles.append(Tile(pygame.Vector2(x, y)))
        return tiles

    def update_tiles(self):
        for tile in self.tiles:
            tile.update(self.mouse)
            if tile.make_buttons:
                self.tile_buttons = self.init_tile_buttons(tile)
        for button in self.tile_buttons:
            button.update(self.mouse)
            if button.clicked:
                self.textures["map"].blit(self.make_cover(), button.tile.pos)
                if button.type == "archer":
                    self.towers.append(ArcherTower(pygame.Vector2(button.tile.pos.x, button.tile.pos.y - 20)))
                    self.tiles.remove(button.tile)
                elif button.type == "mage":
                    pass
                else:
                    self.towers.append(ArtilleryTower(pygame.Vector2(button.tile.pos.x, button.tile.pos.y - 20)))
                    self.tiles.remove(button.tile)
                self.tile_buttons = []

    def update_towers(self):
        for tower in self.towers:
            tower.update(self.enemies)
            if tower.shoot and isinstance(tower, ArcherTower):
                self.projectiles.append(Arrow(pygame.Vector2(tower.pos.x + 10, tower.pos.y + 5), tower.target))
            elif tower.shoot and isinstance(tower, ArtilleryTower):
                self.projectiles.append(Bomb(pygame.Vector2(tower.pos.x + 10, tower.pos.y + 5), tower.target))

    def update_projectiles(self):
        for projectile in self.projectiles:
            if isinstance(projectile, Bomb):
                projectile.update(self.dt, self.enemies)
            else:
                projectile.update(self.dt)
            if projectile.hit:
                self.projectiles.remove(projectile)

    def init_tile_buttons(self, tile):
        tile_buttons = []
        tile_buttons.append(TileButton(pygame.Vector2(tile.pos.x - 10, tile.pos.y + 7), pygame.Vector2(8, 8), "archer", tile))
        tile_buttons.append(TileButton(pygame.Vector2(tile.pos.x + 6, tile.pos.y - 10), pygame.Vector2(8, 8), "mage", tile))
        tile_buttons.append(TileButton(pygame.Vector2(tile.pos.x + 22, tile.pos.y + 7), pygame.Vector2(8, 8), "artillery", tile))
        return tile_buttons

    def load_map(self):
        return [list(line.rstrip()) for line in open("map.txt", "r").readlines()]

    def get_path(self):
        path = []
        actual_pos = self.find_entrance()
        path.append(pygame.Vector2(actual_pos.x + 1, actual_pos.y))
        while self.map[int(actual_pos.y)][int(actual_pos.x)] != '[':
            ROUNDING = [pygame.Vector2(0, -1), pygame.Vector2(0, 1), pygame.Vector2(-1, 0)]
            for shift in ROUNDING:
                next_pos = actual_pos + shift
                if self.is_valid_field(int(next_pos.y), int(next_pos.x)) and next_pos not in path:
                    if self.map[int(next_pos.y)][int(next_pos.x)] == '#':
                        path.append(actual_pos)
                        actual_pos = next_pos.copy()
                        break
                    elif self.map[int(next_pos.y)][int(next_pos.x)] == '[':
                        path.append(actual_pos)
                        actual_pos = next_pos.copy()
                        break
        path.append(actual_pos)
        path.append(pygame.Vector2(actual_pos.x - 1, actual_pos.y))
        return path

    def is_valid_field(self, y, x):
        return not (x < 0 or x >= DRAW_SCREEN_SIZE.x // BLOCK_SIZE or y < 0 or y >= DRAW_SCREEN_SIZE.y // BLOCK_SIZE)

    def find_entrance(self):
        for y in range(int(DRAW_SCREEN_SIZE.y // BLOCK_SIZE)):
            for x in range(int(DRAW_SCREEN_SIZE.x // BLOCK_SIZE)):
                if self.map[y][x] == ']':
                    return pygame.Vector2(x, y)

    def render_map(self):
        map_surface = pygame.Surface(DRAW_SCREEN_SIZE)
        for y, line in enumerate(self.map):
            for x, tile in enumerate(line):
                if tile == '/':
                    texture = self.textures["grass" + str(random.randint(1, 9))]
                elif tile in ['#', '[', ']']:
                    texture = self.textures["path"]
                map_surface.blit(texture, pygame.Vector2(x, y) * BLOCK_SIZE)
        for y, line in enumerate(self.map):
            for x, tile in enumerate(line):
                if tile == '*':
                    map_surface.blit(self.textures["tileDark"], pygame.Vector2(x, y) * BLOCK_SIZE)
        return map_surface

    def make_cover(self):
        cover = pygame.Surface(pygame.Vector2(BLOCK_SIZE, BLOCK_SIZE) * 2)
        cover.blit(self.textures["grass" + str(random.randint(1, 9))], pygame.Vector2(0, 0))
        cover.blit(self.textures["grass" + str(random.randint(1, 9))], pygame.Vector2(BLOCK_SIZE, 0))
        cover.blit(self.textures["grass" + str(random.randint(1, 9))], pygame.Vector2(0, BLOCK_SIZE))
        cover.blit(self.textures["grass" + str(random.randint(1, 9))], pygame.Vector2(BLOCK_SIZE, BLOCK_SIZE))
        return cover

    def load_textures(self):
        for texture_name in os.listdir("Textures"):
            texture = image.load("Textures/" + texture_name)
            self.textures[texture_name.replace(".png", "")] = texture
        self.textures["map"] = self.render_map()


if __name__ == '__main__':
    Main()

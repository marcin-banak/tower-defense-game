"""Główny moduł gry. Używa pozostałych modułów projektu. Uruchomienie
tego modułu skutkuje uruchomieniem menu gry.
"""

import time
import os

from pygame import *

from Footman import *
from CONST import *
from Knight import *
from Wolf import *
from ArcherTower import *
from Arrow import *
from ArtilleryTower import *
from Bomb import *
from MageTower import *
from Beam import *
from mouse import *
from Tile import *
from TileButton import *
from Button import *


class Main:
    """Główna klasa programu. Odpowiada za przygotowanie elementów gry, obsługę
    głównej pętli gry oraz rysowanie.

    Attributes:
        screen (pygame.Surface): Płaszczyzna ekranu, \
        na której wyświetlany jest program.

        draw_screen (pygame.Surface): Płaszczyzna, \
        na której rysowany jest program.

        font (pygame.font): Czcionka napisów używanych przez program.

        map (list): Lista napisów, w której prztrzymywana jest mapa \
        wczytana z pliku tekstowego.

        textures (dict): Słownik przetrzymujący tekstury programu.

        mouse (mouse.Mouse): Obiekt myszki.

        is_running (bool): Zmienna determinująca długość działania \
        głównej pętli programu.

        clock (pygame.Clock): Obiekt zegara służący do obliczania czasu \
        jaki minął pomiędzy klatkami.

        dt (float): Skalar, przez który przemnażane są zmienne, \
        aby zadbać o jednolite działanie programu, \
        niezależnie od prędkości jego działania.

        path (list): Lista, w której przechowywane są pary koordynatów \
        kolejnych pól ścieżki.

        enemies (list): Lista przechowująca obiekty przeciwników.

        tiles (list): Lista przechowująca obiekty pól wież.

        tile_buttons (list): Lista przechowująca przyciski do wyboru wieży.

        towers (list): Lista przechowująca obiekty wież.

        projectiles (list): Lista przechowująca obiekty pocisków.

        enemies_power (int): Zmienna śledząca sumę siły przeciwników \
        znajdujących się w grze.

        base_HP (int): Zmienna przechowująca obecną ilość punktów życia bazy.

        buttons (list): Lista przycisków znajdujących się w menu.
    """
    def __init__(self):
        """inicjowanie programu.

        Returns: void
        """
        init()
        self.screen: pygame.Surface = display.set_mode(SCREEN_SIZE)
        self.draw_screen: pygame.Surface = pygame.Surface(DRAW_SCREEN_SIZE)
        self.font: pygame.font = pygame.font.Font("font.ttf", 14)
        display.set_caption("Tower defense")

        self.map: list = []
        self.map = self.load_map()
        self.textures: dict = {}
        self.load_textures()
        self.mouse: mouse.Mouse = Mouse()
        self.is_running: bool = True
        self.clock: pygame.Clock = time.Clock()
        self.dt: float = 1

        self.path: list = []
        self.enemies: list = []
        self.tiles: list = []
        self.tile_buttons: list = []
        self.towers: list = []
        self.projectiles: list = []
        self.enemies_power: int = None
        self.base_HP: int = None

        self.buttons: list = []
        self.init_menu()

        while self.is_running:
            self.check_events()
            self.scene()
            self.display_update()
        quit()

    def check_events(self):
        """
        Sprawdzenie czy w trakcie działania programu zostało stworzone zdarzenie z modułu pygame
        i wykonanie powiązanych z nim akcji.

        Returns: void
        """
        self.mouse.update(SCREEN_SIZE)
        for e in event.get():
            if e.type == QUIT:
                self.is_running = False

    def display_update(self):
        """
        Odświeżenie ekranu i wyrysowanie wszystkich zmian, które zaszły od narysowania poprzedniej klatki.

        Returns: void
        """
        self.dt = self.clock.tick(FPS) * 60 / 1000
        self.screen.blit(pygame.transform.scale(self.draw_screen, SCREEN_SIZE), (0, 0))
        display.update()

    def init_menu(self):
        """
        Zainicjowanie zasobów używanych do obsługi menu.

        Returns: void
        """
        self.buttons = self.init_buttons()
        self.scene = self.menu

    def menu(self):
        """
        Obsłużenie logiki związanej z działeniem menu.

        Returns: void
        """
        self.update_buttons()
        self.draw_menu()

    def draw_menu(self):
        """
        Narysowanie menu po wcześniejszym obliczeniu go przez metodę menu.

        Returns: void
        """
        self.draw_screen.fill((0, 0, 0))
        for button in self.buttons:
            self.draw_screen.blit(self.textures["startButton"], button.pos)

    def init_buttons(self):
        """
        Zainicjowania listy przycisków znajdujących się w menu.

        Returns: buttons: list
        """
        buttons = []
        buttons.append(Button(pygame.Vector2(115, 75), pygame.Vector2(90, 30)))
        return buttons

    def update_buttons(self):
        """
        Zaktualizowanie przycisków znajdujących się w menu.

        Returns: void
        """
        for button in self.buttons:
            button.update(self.mouse)
            if button.clicked:
                self.init_game()

    def init_game(self):
        """
        Zainicjowanie zasobów używanych do obsługi gry.

        Returns: void
        """
        self.path = self.get_path()
        self.enemies = self.init_enemies()
        self.tiles = self.init_tiles()
        self.base_HP = 20
        self.scene = self.game

    def game(self):
        """
        Obsłużenie logiki związanej z działeniem gry.

        Returns: void
        """
        self.update_enemies()
        self.update_tiles()
        self.update_towers()
        self.update_projectiles()

        if self.base_HP <= 0:
            self.init_menu()
            self.scene = self.menu
        self.draw_game()

    def draw_game(self):
        """
        Narysowanie gry po wcześniejszym obliczeniu jej przez metodę game.

        Returns: void
        """
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
            else:
                self.draw_screen.blit(self.textures["mage"], tower.pos)
        for projectile in self.projectiles:
            if isinstance(projectile, Arrow):
                self.draw_screen.blit(self.textures["arrow"], projectile.pos)
            elif isinstance(projectile, Bomb):
                self.draw_screen.blit(self.textures["bomb"], projectile.pos)
            else:
                self.draw_screen.blit(self.textures["beam"], projectile.pos)
        self.draw_screen.blit(self.textures["statusBar"], pygame.Vector2(0, 0))
        self.draw_screen.blit(self.font.render(str(self.base_HP), True, pygame.Color(255, 255, 255)), pygame.Vector2(14, 2))

    def init_enemies(self):
        """
        Zainicjowanie listy przeciwników.

        Returns: enemies: list
        """
        enemies = []
        enemies.append(Knight(self.path[0]))
        for i in range(5):
            enemies.append(Footman(pygame.Vector2((self.path[0].x + i + 1), self.path[0].y)))
        enemies.append(Wolf(self.path[0]))
        self.enemies_power = WOLF_POWER + 5 * FOOTMAN_POWER + KNIGHT_POWER
        return enemies

    def add_enemies(self):
        """
        Dodanie przeciwników do listy enemies na podstawie stałych
        ENEMIES_MAX_POWER i ENEMIES_POWER_INTERVAL.

        Returns: void
        """
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
        """
        Zakutalizowanie przeciwników.

        Returns: void
        """
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
        """
        Zainicjowanie listy pól wież.

        Returns: tiles: list
        """
        tiles = []
        for y in range(int(DRAW_SCREEN_SIZE.y // BLOCK_SIZE)):
            for x in range(int(DRAW_SCREEN_SIZE.x // BLOCK_SIZE)):
                if self.map[y][x] == '*':
                    tiles.append(Tile(pygame.Vector2(x, y)))
        return tiles

    def update_tiles(self):
        """
        Zaktualizowanie pól wież.

        Returns: void
        """
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
                    self.towers.append(MageTower(pygame.Vector2(button.tile.pos.x, button.tile.pos.y - 20)))
                    self.tiles.remove(button.tile)
                else:
                    self.towers.append(ArtilleryTower(pygame.Vector2(button.tile.pos.x, button.tile.pos.y - 20)))
                    self.tiles.remove(button.tile)
                self.tile_buttons = []

    def update_towers(self):
        """
        Zaktualizowanie wież.

        Returns: void
        """
        for tower in self.towers:
            tower.update(self.enemies)
            if tower.shoot and isinstance(tower, ArcherTower):
                self.projectiles.append(Arrow(pygame.Vector2(tower.pos.x + 10, tower.pos.y + 5), tower.target))
            elif tower.shoot and isinstance(tower, ArtilleryTower):
                self.projectiles.append(Bomb(pygame.Vector2(tower.pos.x + 10, tower.pos.y + 5), tower.target))
            elif tower.shoot and isinstance(tower, MageTower):
                self.projectiles.append(Beam(pygame.Vector2(tower.pos.x + 10, tower.pos.y + 5), tower.target))

    def update_projectiles(self):
        """
        Zaktualizowanie pocisków.

        Returns: void
        """
        for projectile in self.projectiles:
            if isinstance(projectile, Bomb):
                projectile.update(self.dt, self.enemies)
            else:
                projectile.update(self.dt)
            if projectile.hit:
                self.projectiles.remove(projectile)

    def init_tile_buttons(self, tile: Tile):
        """
        Utworzenie przycisków, które pokazują się po naciśnięciu pola wieży.

        Args: tile (Tile)
        Returns: tile_buttons (list)
        """
        tile_buttons = []
        tile_buttons.append(TileButton(pygame.Vector2(tile.pos.x - 10, tile.pos.y + 7), pygame.Vector2(8, 8), "archer", tile))
        tile_buttons.append(TileButton(pygame.Vector2(tile.pos.x + 6, tile.pos.y - 10), pygame.Vector2(8, 8), "mage", tile))
        tile_buttons.append(TileButton(pygame.Vector2(tile.pos.x + 22, tile.pos.y + 7), pygame.Vector2(8, 8), "artillery", tile))
        return tile_buttons

    def load_map(self):
        """
        Wczytanie mapy z pliku tekstowego.

        Returns: map (list)
        """
        return [list(line.rstrip()) for line in open("map.txt", "r").readlines()]

    def get_path(self):
        """
        Stworzenie listy koordynatów reprezentujących pola ścieżki.

        Returns: path (list)
        """
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

    def is_valid_field(self, y: int, x: int):
        """
        Sprawdzenie czy podane koordynaty x i y mieszczą się w rozmiarach mapy.

        Args:
            y (int)
            x (int)
        Returns:
             is_valid_field (bool)
        """
        return not (x < 0 or x >= DRAW_SCREEN_SIZE.x // BLOCK_SIZE or y < 0 or y >= DRAW_SCREEN_SIZE.y // BLOCK_SIZE)

    def find_entrance(self):
        """
        Znalezienie pola, które jest początkiem ścieżki.

        Returns: entrance (pygame.Vector2)
        """
        for y in range(int(DRAW_SCREEN_SIZE.y // BLOCK_SIZE)):
            for x in range(int(DRAW_SCREEN_SIZE.x // BLOCK_SIZE)):
                if self.map[y][x] == ']':
                    return pygame.Vector2(x, y)

    def render_map(self):
        """
        Narysowanie mapy na podstawie tekstur gry i pliku tekstowego z mapą.

        Returns: map_surface (pygame.Surface)
        """
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
        """
        Stworzenie płaszczyzny która przysłoni pole wieży po jej zbudowaniu.

        Returns: cover (pygame.Surface)
        """
        cover = pygame.Surface(pygame.Vector2(BLOCK_SIZE, BLOCK_SIZE) * 2)
        cover.blit(self.textures["grass" + str(random.randint(1, 9))], pygame.Vector2(0, 0))
        cover.blit(self.textures["grass" + str(random.randint(1, 9))], pygame.Vector2(BLOCK_SIZE, 0))
        cover.blit(self.textures["grass" + str(random.randint(1, 9))], pygame.Vector2(0, BLOCK_SIZE))
        cover.blit(self.textures["grass" + str(random.randint(1, 9))], pygame.Vector2(BLOCK_SIZE, BLOCK_SIZE))
        return cover

    def load_textures(self):
        """
        Wczytanie tekstur programu.

        Returns: void
        """
        for texture_name in os.listdir("Textures"):
            texture = image.load("Textures/" + texture_name)
            self.textures[texture_name.replace(".png", "")] = texture
        self.textures["map"] = self.render_map()


if __name__ == '__main__':
    Main()

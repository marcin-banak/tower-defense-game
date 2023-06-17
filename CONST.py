# -----------------------------------------------------------------------------
# Marcin Banak
# Zadanie końcowe na przedmiot "Programowanie obiektowe"
# Gra "Tower defense"
# Data utworzenia: 14.06.2023
# Wersja 1.0.0
# -----------------------------------------------------------------------------

"""Moduł zawiera stałe wykorzystywane przez program."""
import pygame

WIDTH = 1024
"""Szerokość ekranu."""
HEIGHT = 576
"""Wysokość ekranu."""
BLOCK_SIZE = 10
"""Wielkość bloków mapy."""
SCREEN_SIZE = pygame.Vector2(WIDTH, HEIGHT)
"""Wektor przechowujący rozdzielczość wyświetlacza."""
DRAW_SCREEN_SIZE = pygame.Vector2(320, 180)
"""Wektor przechowujący rozdzielczość płaszczyzny, na której rysuje program."""
TILE_SIZE = pygame.Vector2(20, 20)
"""Wektor przechowujący wymiary pola wieży."""
FPS = 60
"""Ilość klatek na sekundę."""
MOVE_PRECISION = 3
"""Prezycja z jaką wykrywane są kolizje."""
BASE_PRECISION = 7
"""Precyzja z jaką wykrywana jest kolizja przeciwnika z bazą."""

FOOTMAN_HP = 120
"""Początkowy stan punktów życia obiektu klasy Footman."""
FOOTMAN_SPEED = 0.2
"""Prędkość przemieszczania się obiektu klasy Footman."""
FOOTMAN_BASE_DAMAGE = 1
"""Wartość obrażeń zadawanych przez obiekt klasy Footman, jeśli dotrze on do pola bazy."""
FOOTMAN_ANIMATION_TIME = 0.3
"""Prędkość z jaką zmieniają się klatki animacji obiektu klasy Footman."""
FOOTMAN_POWER = 5
"""Siła przeciwnika klasy Footman wykorzystwana do obliczenia momentu wygenerowania nowej fali przeciwników."""

KNIGHT_HP = 300
"""Początkowy stan punktów życia obiektu klasy Knight."""
KNIGHT_SPEED = 0.07
"""Prędkość przemieszczania się obiektu klasy Knight."""
KNIGHT_BASE_DAMAGE = 3
"""Wartość obrażeń zadawanych przez obiekt klasy Knight, jeśli dotrze on do pola bazy."""
KNIGHT_ANIMATION_TIME = 0.2
"""Prędkość z jaką zmieniają się klatki animacji obiektu klasy Knight."""
KNIGHT_POWER = 18
"""Siła przeciwnika klasy Knight wykorzystwana do obliczenia momentu wygenerowania nowej fali przeciwników."""

WOLF_HP = 80
"""Początkowy stan punktów życia obiektu klasy Wolf."""
WOLF_SPEED = 0.3
"""Prędkość przemieszczania się obiektu klasy Wolf."""
WOLF_BASE_DAMAGE = 1
"""Wartość obrażeń zadawanych przez obiekt klasy Wolf, jeśli dotrze on do pola bazy."""
WOLF_ANIMATION_TIME = 0.2
"""Prędkość z jaką zmieniają się klatki animacji obiektu klasy Wolf."""
WOLF_POWER = 9
"""Siła przeciwnika klasy Wolf wykorzystwana do obliczenia momentu wygenerowania nowej fali przeciwników."""

ENEMIES_MIN_POWER = KNIGHT_POWER
"""Minimalna siła przciwników na podstawie której wybierany jest moment generowania fali."""
ENEMIES_MAX_POWER = 5 * KNIGHT_POWER
"""Maksymalna siła przciwników na podstawie której generowani są przeciwnicy."""
ENEMIES_POWER_INTERVAL = 12
"""Stała na podstawie której losowana jest maksymalna siła przeciwników w danej fali."""
ENEMIES_SUM_POWER = FOOTMAN_POWER + WOLF_POWER + KNIGHT_POWER
"""Suma siły wszytkich przeciwników służąca do obliczenia prawdopodobieństwa wystąpienia przeciwnika w danej fali."""

TOWER_SIZE = pygame.Vector2(20, 40)
"""Wektor przechowujący wymiary wieży."""

ARCHER_TOWER_RANGE = 70
"""Zasięg obiektu klasy ArcherTower służący do określenia czy przeciwnik znajduje się w jej zasięgu."""
ARCHER_TOWER_SPEED = 1
"""Prędkość z jaką obiket klasy ArcherTower może wystrzelić pocisk."""
ARROW_SPEED = 1
"""Prędkość przemieszczania się pocisku typu ."""
ARROW_DAMAGE = 12
"""Obrażenia zadawane przez pocisk typu Arrow."""

MAGE_TOWER_RANGE = 65
"""Zasięg obiektu klasy MageTower służący do określenia czy przeciwnik znajduje się w jej zasięgu."""
MAGE_TOWER_SPEED = 1.9
"""Prędkość z jaką obiket klasy MageTower może wystrzelić pocisk."""
BEAM_SPEED = 1.4
"""Prędkość przemieszczania się pocisku typu Beam."""
BEAM_DAMAGE = 38
"""Obrażenia zadawane przez pocisk typu Beam."""

ARTILLERY_TOWER_RANGE = 50
"""Zasięg obiektu klasy ArtilleryTower służący do określenia czy przeciwnik znajduje się w jej zasięgu."""
ARTILLERY_TOWER_SPEED = 2.4
"""Prędkość z jaką obiket klasy ArtilleryTower może wystrzelić pocisk."""
BOMB_SPEED = 0.9
"""Prędkość przemieszczania się pocisku typu Bomb."""
BOMB_DAMAGE = 37
"""Obrażenia zadawane przez pocisk typu Bomb."""
BOMB_SPLASH_AREA = 15
"""Obszar, w którym pocisk typu Bomb zadaje obrażenia."""


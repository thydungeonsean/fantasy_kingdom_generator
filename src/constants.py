from pygame.locals import *


SCALE = 1

# SCREENW = 640 * SCALE
# SCREENH = 360 * SCALE
SCREENW = 1280
SCREENH = 720

BASE_TILE_W = 24
BASE_TILE_H = 24

TILEW = BASE_TILE_W * SCALE
TILEH = BASE_TILE_H * SCALE

BASE_UNIT_W = 16
BASE_UNIT_H = 24

UNITW = BASE_UNIT_W * SCALE
UNITH = BASE_UNIT_H * SCALE

DISPLAY_W = SCREENW / TILEW
DISPLAY_H = SCREENH / TILEH

FPS = 60

# terrain

WATER = 0
SWAMP = 2
LOWLAND = 3
HIGHLAND = 4
DESERT = 5
ROUGH = 6
FOREST = 7
RIVER = 8
MOUNTAIN = 9

# terrain animation
WATER_B = 10

# buildings
CAPITOL = 11
SETTLEMENT = 12

# map objects
ARMY = 15
NAVY = 16

# colors

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SHADE = (50, 50, 50)

COLORKEY = WHITE

# nation colors
RED = (255, 0, 0)
DARK_RED = (150, 0, 0)
ORANGE = (255, 150, 0)
YELLOW = (255, 255, 0)
GOLD = (150, 150, 0)
LIGHT_GREEN = (0, 250, 0)
DARK_GREEN = (0, 150, 0)
BLUE = (0, 0, 250)
DARK_BLUE = (0, 0, 150)
CYAN = (0, 255, 255)
MED_CYAN = (0, 150, 255)
DARK_CYAN = (0, 150, 150)
PURPLE = (150, 0, 255)
DARK_PURPLE = (150, 0, 150)
MAGENTA = (255, 0, 250)
# GREY = (150, 150, 150)
# PLAYER_BLACK = (0, 0, 0)
# PLAYER_WHITE = (255, 255, 255)

PLAYER_COLORS = (RED, DARK_RED, ORANGE, YELLOW, GOLD, LIGHT_GREEN, DARK_GREEN, BLUE, DARK_BLUE,
                 CYAN, MED_CYAN, DARK_CYAN, PURPLE, DARK_PURPLE, MAGENTA) #, GREY, PLAYER_BLACK, PLAYER_WHITE)

# keys
UP = K_w
DOWN = K_s
LEFT = K_a
RIGHT = K_d
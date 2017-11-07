from src.constants import *
import pygame


tiles = {
    # key: (tilesheet offset in tiles)
    WATER: (0, 0),
    SWAMP: (2, 1),
    LOWLAND: (2, 0),
    HIGHLAND: (3, 0),
    DESERT: (3, 1),
    ROUGH: (4, 1),
    FOREST: (1, 1),
    RIVER: (0, 0),
    MOUNTAIN: (4, 0),

    # building tile keys
    CAPITOL: (0, 2),
    SETTLEMENT: (1, 2),

    # map objects tile keys
    ARMY: (2, 2),
    NAVY: (3, 2),
}

units = {
    'centaur_spear': (0, 0),
    'centaur_archer': (1, 0),
    'centaur_knight': (2, 0),
    'centaur_chief': (3, 0),

    'naga_soldier': (4, 0),
    'naga_archer': (5, 0),
    'naga_mage': (6, 0),

    'ogre_grunt': (7, 0),
    'ogre_soldier': (8, 0),
    'ogre_magi': (9, 0),

    'goblin_grunt': (0, 2),
    'goblin_archer': (1, 2),
    'goblin_chief': (2, 2),

    'kobold_warrior': (3, 2),
    'kobold_archer': (4, 2),
    'kobold_chief': (5, 2),

    'avian_scout': (6, 2),
    'avian_warrior': (7, 2),

    'dark_elf_scout': (8, 2),
    'dark_elf_warrior': (9, 2),
    'spider': (10, 2),

    'zombie': (0, 4),
    'skeleton_warrior': (1, 4),
    'skeleton_archer': (2, 4),
    'necromancer': (3, 4),

    'ratling_warrior': (4, 4),
    'ratling_archer': (5, 4),

    'orc_soldier': (6, 4),
    'orc_berserker': (7, 4),
    'orc_axe': (8, 4),

    'gnome': (0, 6),
    'gnome_magician': (1, 6),

    'fey': (2, 6),
    'fey_warrior': (3, 6),
    'fey_enchanter': (4, 6),

    'dwarf_soldier': (5, 6),
    'dwarf_berserker': (6, 6),
    'dwarf_champion': (7, 6),

    'halfling_slinger': (8, 6),
    'halfling_soldier': (9, 6),
    'halfling_magician': (10, 6),

    'minotaur': (0, 8),

    'elf_warrior': (1, 8),
    'elf_ranger': (2, 8),
    'elf_druid': (3, 8),
    'treant': (4, 8),

    'barbarian_archer': (0, 10),
    'barbarian_warrior': (1, 10),
    'barbarian_berserker': (2, 10),
    'barbarian_cavalry': (6, 12),

    'knight_archer': (3, 10),
    'knight_templar': (4, 10),
    'knight_soldier': (5, 10),
    'knight_cavalry': (6, 10),

    'citizen_archer': (0, 12),
    'citizen_legionary': (1, 12),
    'citizen_acolyte': (2, 12),
    'citizen_cavalry': (6, 12),

    'nomad_archer': (3, 12),
    'nomad_warrior': (4, 12),
    'nomad_mage': (5, 12),
    'nomad_cavalry': (6, 12),
}


for (k, (x, y)) in units.items()[:]:
    b_key = ''.join((k, '_b'))
    units[b_key] = (x, y+1)


tile_sheet = None
tile_rect = pygame.Rect((0, 0), (TILEW, TILEH))

unit_sheet = None
unit_rect = pygame.Rect((0, 0), (UNITW, UNITH))


def load_tile_sheet():

    global tile_sheet

    if tile_sheet is None:
        tile_sheet = pygame.image.load('assets\\tiles.png').convert()

    return tile_sheet


def load_unit_sheet():

    global unit_sheet

    if unit_sheet is None:
        unit_sheet = pygame.image.load('assets\\sprites.png').convert()

    return unit_sheet

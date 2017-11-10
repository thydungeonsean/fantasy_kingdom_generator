from src.map.height_map import HeightMap
from src.map.terrain_map import TerrainMap
from river_generator import RiverGenerator
from forest_generator import ForestGenerator
from swamp_generator import SwampGenerator
from desert_generator import DesertGenerator
from src.constants import *
from random import randint
from progress_bar import ProgressBar


class MapGenerator(object):

    MAP_W = 120
    MAP_H = 120

    ROUGHNESS = 10

    @classmethod
    def generate_height_map(cls, seed=None):

        cls.draw_load_bar('GENERATING HEIGHT MAP', .0)
        return HeightMap(cls.MAP_W, cls.MAP_H, seed=seed)

    @classmethod
    def generate_terrain_map(cls, height_map):

        cls.draw_load_bar('GENERATING TERRAIN MAP', .05)
        terrain = TerrainMap(height_map)

        cls.draw_load_bar('SEEDING FORESTS', .1)
        ForestGenerator.generate_forests(terrain)

        cls.draw_load_bar('GROWING DESERTS', .2)
        DesertGenerator.generate_desert(terrain)

        cls.draw_load_bar('FLOODING RIVERS', .3)
        RiverGenerator.generate_rivers(terrain)

        cls.draw_load_bar('FORMING SWAMPS', .4)
        SwampGenerator.generate_swamp(terrain)

        cls.draw_load_bar('ADDING ROUGH TERRAIN', .5)
        cls.add_rough_terrain(terrain)

        return terrain

    @classmethod
    def add_rough_terrain(cls, terrain):

        highlands = terrain.get_all(HIGHLAND)

        for point in highlands:
            roll = randint(0, 99)
            if roll < cls.ROUGHNESS:
                terrain.set_tile(point, ROUGH)

    @classmethod
    def draw_load_bar(cls, message, progress):
        ProgressBar.draw_load_bar(message, progress)

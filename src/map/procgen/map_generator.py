from src.map.height_map import HeightMap
from src.map.terrain_map import TerrainMap
from river_generator import RiverGenerator
from forest_generator import ForestGenerator
from swamp_generator import SwampGenerator
from desert_generator import DesertGenerator
from src.constants import *
from random import randint


class MapGenerator(object):

    MAP_W = 120
    MAP_H = 120

    ROUGHNESS = 10

    @classmethod
    def generate_height_map(cls, seed=None):

        return HeightMap(cls.MAP_W, cls.MAP_H, seed=seed)

    @classmethod
    def generate_terrain_map(cls, height_map):

        terrain = TerrainMap(height_map)
        ForestGenerator.generate_forests(terrain)
        DesertGenerator.generate_desert(terrain)
        RiverGenerator.generate_rivers(terrain)
        SwampGenerator.generate_swamp(terrain)

        cls.add_rough_terrain(terrain)

        return terrain

    @classmethod
    def add_rough_terrain(cls, terrain):

        highlands = terrain.get_all(HIGHLAND)

        for point in highlands:
            roll = randint(0, 99)
            if roll < cls.ROUGHNESS:
                terrain.set_tile(point, ROUGH)

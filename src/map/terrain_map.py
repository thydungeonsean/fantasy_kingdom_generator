from _map import _Map
from src.constants import *


class TerrainMap(_Map):

    height_to_terrain = {
        0: WATER,
        1: LOWLAND,
        45: HIGHLAND,
        80: MOUNTAIN,
        # 98: PEAK,
    }

    terrain_to_height = {v: k for k, v in height_to_terrain.iteritems()}

    LAND = {LOWLAND, SWAMP, FOREST, HIGHLAND, ROUGH, DESERT, MOUNTAIN, RIVER}

    def __init__(self, height_map):

        _Map.__init__(self, height_map.w, height_map.h)

        self.height_map = height_map
        self.terrain_map = self.initialize_terrain_map()

        self.translate_height_map()

    def initialize_terrain_map(self):

        terrain_map = [[0 for y in range(self.h)] for x in range(self.w)]

        return terrain_map

    def translate_height_map(self):

        for x, y in self.all_points:

            self.set_tile((x, y), self.translate_point((x, y)))

    def translate_point(self, (x, y)):

        height = self.height_map.get_height((x, y))

        value = 0

        for key in sorted(TerrainMap.height_to_terrain.keys()):

            if height >= key:
                value = TerrainMap.height_to_terrain[key]

        return value

    def set_tile(self, (x, y), terrain):
        self.terrain_map[x][y] = terrain

    def get_tile(self, (x, y)):
        return self.terrain_map[x][y]

    def get_all(self, terrain):
        if isinstance(terrain, tuple):
            return filter(lambda p: self.get_tile(p) in terrain, self.all_points)
        else:
            return filter(lambda p: self.get_tile(p) == terrain, self.all_points)

    def adj_to_water(self, point):

        adj = self.get_adj(point)
        for point in adj:
            if self.get_tile(point) == WATER:
                return True
        return False

    @property
    def all_land(self):
        for y in range(self.h):
            for x in range(self.w):
                if self.get_tile((x, y)) in TerrainMap.LAND:
                    yield x, y

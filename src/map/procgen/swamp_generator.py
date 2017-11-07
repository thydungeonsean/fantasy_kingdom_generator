from automata_terrain_generator import AutomataTerrainGenerator
from random import *
from src.constants import *
from src.map.terrain_map import TerrainMap


class SwampGenerator(AutomataTerrainGenerator):

    NUMBER_OF_SWAMPS = 10
    SWAMP_SIZE = 12
    VALID_FOR_SWAMP = LOWLAND, RIVER, FOREST
    VALID_HEIGHT = TerrainMap.terrain_to_height[HIGHLAND] - 1

    BUFFER_FROM_DESERT = 8

    @classmethod
    def generate_swamp(cls, terrain):

        valid_swamp_points = cls.find_valid_swamp_points(terrain)
        # get spaces valid for swamp seeds
        valid_seed_points = cls.find_valid_seed_points(terrain, valid_swamp_points)

        swamp_map = cls.create_new_automata_map(terrain)
        # place swamp seeds
        cls.place_swamp_seeds(swamp_map, valid_seed_points)

        # grow swamps
        for i in range(cls.SWAMP_SIZE):
            cls.run_swamp_automata(swamp_map, terrain, valid_swamp_points)

        cls.form_swamps(terrain, swamp_map, valid_swamp_points)

    @classmethod
    def find_valid_seed_points(cls, terrain, valid):

        def is_desert_border((x, y)):

            adj = ((x+1, y), (x-1, y), (x, y+1), (x, y-1))
            for a in adj:
                if terrain.get_tile(a) not in (DESERT, WATER):
                    return True
            return False

        desert_borders = filter(is_desert_border, terrain.get_all(DESERT))

        too_close_to_desert = cls.get_points_too_close_to_desert(desert_borders)

        return list(filter(lambda x: x not in too_close_to_desert, valid))

    @classmethod
    def find_valid_swamp_points(cls, terrain):
        def valid_height((x, y)):
            return terrain.height_map.get_height((x, y)) <= cls.VALID_HEIGHT

        valid = filter(valid_height, terrain.get_all(cls.VALID_FOR_SWAMP))
        return valid

    @classmethod
    def get_points_too_close_to_desert(cls, desert_borders):

        too_close = set()

        for (x, y) in desert_borders:

            for mx in range(-cls.BUFFER_FROM_DESERT, cls.BUFFER_FROM_DESERT+1):
                for my in range(-cls.BUFFER_FROM_DESERT, cls.BUFFER_FROM_DESERT+1):
                    too_close.add((mx+x, my+y))

        return too_close

    @classmethod
    def place_swamp_seeds(cls, swamp_map, valid_seed_points):

        seeds = sample(valid_seed_points, cls.NUMBER_OF_SWAMPS)

        def set_to_swamp((x, y)):
            swamp_map[x][y] = True

        map(set_to_swamp, seeds)

    @classmethod
    def run_swamp_automata(cls, swamp_map, terrain, valid_swamp):

        spread_list = []
        for x, y in valid_swamp:
            if not swamp_map[x][y]:
                spread = cls.swamp_tile_spreads((x, y), swamp_map, terrain)
                if spread:
                    spread_list.append((x, y))

        def set_to_swamp((x, y)):
            swamp_map[x][y] = True

        map(set_to_swamp, spread_list)

        return swamp_map

    @classmethod
    def swamp_tile_spreads(cls, (x, y), swamp_map, terrain):

        def is_swamp((x, y)):
            return swamp_map[x][y]

        spread_chance = 0

        orth_adj = terrain.get_adj((x, y))
        for point in orth_adj:
            if is_swamp(point):
                spread_chance += 30

        if spread_chance == 0:
            return False

        if terrain.get_tile((x, y)) == FOREST:
            spread_chance -= 10
        elif terrain.get_tile((x, y)) == RIVER:
            spread_chance += 10

        diag_adj = cls.get_diagonal_adj((x, y), terrain)
        for point in diag_adj:
            if is_swamp(point):
                spread_chance += 5

        roll = randint(0, 99)

        return roll < spread_chance

    @classmethod
    def get_diagonal_adj(cls, (x, y), terrain):

        adj = [(x-1, y-1), (x+1, y-1), (x-1, y+1), (x+1, y+1)]
        return filter(terrain.point_in_bounds, adj)

    @classmethod
    def form_swamps(cls, terrain, swamp_map, valid):

        for x, y in valid:
            if swamp_map[x][y]:
                if terrain.get_tile((x, y)) != RIVER:
                    terrain.set_tile((x, y), SWAMP)

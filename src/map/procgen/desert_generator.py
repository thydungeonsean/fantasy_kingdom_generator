from src.constants import *
from automata_terrain_generator import AutomataTerrainGenerator
from random import *


class DesertGenerator(AutomataTerrainGenerator):

    VALID_DESERT_TERRAIN = LOWLAND, HIGHLAND, FOREST
    DESERT_SIZE = 12
    NUM_DESERTS = 4

    @classmethod
    def generate_desert(cls, terrain):

        desert_map = cls.create_new_automata_map(terrain)

        cls.find_desert_seed_points(terrain, desert_map)

        for i in range(cls.DESERT_SIZE):
            cls.run_desert_automata(desert_map, terrain)

        cls.choose_largest_deserts(desert_map, terrain)

        cls.form_deserts(terrain, desert_map)

    @classmethod
    def find_desert_seed_points(cls, terrain, desert_map):

        highland = terrain.get_all(HIGHLAND)

        seeds = filter(lambda x: cls.is_good_desert_seed_point(terrain, x), highland)

        def set_to_desert((x, y)):
            desert_map[x][y] = True

        map(set_to_desert, seeds)

    @classmethod
    def is_good_desert_seed_point(cls, terrain, (x, y)):

        above = x, y-1
        right = x+1, y
        in_bounds = len(filter(terrain.point_in_bounds, (above, right))) == 2

        return in_bounds and terrain.get_tile(above) == MOUNTAIN and terrain.get_tile(right) == MOUNTAIN

    @classmethod
    def form_deserts(cls, terrain, desert_map):

        for x, y in terrain.all_land:
            if desert_map[x][y]:
                terrain.set_tile((x, y), DESERT)

    @classmethod
    def run_desert_automata(cls, desert_map, terrain):

        spread_list = []
        for x, y in terrain.all_land:
            if not desert_map[x][y]:
                spread = cls.desert_tile_spreads((x, y), desert_map, terrain)
                if spread:
                    spread_list.append((x, y))

        def set_to_desert((x, y)):
            desert_map[x][y] = True

        map(set_to_desert, spread_list)

        return desert_map

    @classmethod
    def desert_tile_spreads(cls, (x, y), desert_map, terrain):

        def is_desert((x, y)):
            return desert_map[x][y]

        if terrain.get_tile((x, y)) not in cls.VALID_DESERT_TERRAIN:
            return False

        spread_chance = 0

        orth_adj = terrain.get_adj((x, y))
        for point in orth_adj:
            if is_desert(point):
                spread_chance += 30

        if spread_chance == 0:
            return False

        diag_adj = cls.get_diagonal_adj((x, y), terrain)
        for point in diag_adj:
            if is_desert(point):
                spread_chance += 5

        roll = randint(0, 99)

        return roll < spread_chance

    @classmethod
    def get_diagonal_adj(cls, (x, y), terrain):

        adj = [(x-1, y-1), (x+1, y-1), (x-1, y+1), (x+1, y+1)]
        return filter(terrain.point_in_bounds, adj)

    @classmethod
    def choose_largest_deserts(cls, desert_map, terrain):

        untouched_desert = set()
        desert_zone_dict = {}

        for x, y in terrain.all_land:
            if desert_map[x][y]:
                untouched_desert.add((x, y))

        zone_id = 0

        while untouched_desert:

            cls.flood_desert_zone(untouched_desert, desert_zone_dict, zone_id)
            zone_id += 1

        if len(desert_zone_dict) <= cls.NUM_DESERTS:  # we can use all the deserts
            return

        def size_of_desert_zone(key):

            return len(desert_zone_dict[key])

        # get the biggest deserts
        biggest = sorted(desert_zone_dict.keys(), key=size_of_desert_zone, reverse=True)

        # fill in all the small deserts
        zones_to_be_removed = biggest[cls.NUM_DESERTS:]

        for key in zones_to_be_removed:
            for x, y in desert_zone_dict[key]:
                desert_map[x][y] = False


    @classmethod
    def flood_desert_zone(cls, untouched_desert, desert_zone_dict, zone_id):

        desert_zone_dict[zone_id] = set()
        first = untouched_desert.pop()
        desert_zone_dict[zone_id].add(first)

        edge = [first]
        while edge:

            next_edge = cls.get_next_edge(edge, untouched_desert)
            for point in next_edge:
                untouched_desert.remove(point)
                desert_zone_dict[zone_id].add(point)
            edge = next_edge

    @classmethod
    def get_next_edge(cls, edge, untouched_desert):

        touched = set()

        for point in edge:
            adj = cls.get_adj(point)

            for a in adj:
                if a in untouched_desert:
                    touched.add(a)

        return list(touched)

    @classmethod
    def get_adj(cls, (x, y)):

        return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]







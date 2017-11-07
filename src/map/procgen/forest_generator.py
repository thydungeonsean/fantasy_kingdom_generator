from src.constants import *
from random import *
from automata_terrain_generator import AutomataTerrainGenerator


class ForestGenerator(AutomataTerrainGenerator):

    FOREST_PASSES = 3

    SEEDABLE = LOWLAND, HIGHLAND
    initial_seed_chances = {
        LOWLAND: 35,
        HIGHLAND: 55
    }

    @classmethod
    def generate_forests(cls, terrain):

        forest_map = cls.create_new_automata_map(terrain)

        cls.seed_map(forest_map, terrain)

        for i in range(cls.FOREST_PASSES):
            forest_map = cls.run_forest_automata(forest_map, terrain)

        cls.set_forest_tiles(forest_map, terrain)

    @classmethod
    def set_forest_tiles(cls, forest_map, terrain):

        for x, y in terrain.all_points:
            if forest_map[x][y]:
                terrain.set_tile((x, y), FOREST)

    @classmethod
    def seed_map(cls, forest_map, terrain):
        seedable = filter(lambda x: terrain.get_tile(x) in cls.SEEDABLE, terrain.all_points)
        shuffle(seedable)

        for x, y in seedable:
            chance = cls.initial_seed_chances[terrain.get_tile((x, y))]
            roll = randint(0, 99)
            if roll < chance:
                forest_map[x][y] = True

    @classmethod
    def run_forest_automata(cls, old_forest_map, terrain):

        forest_map = cls.create_new_automata_map(terrain)

        for x, y in terrain.all_land:
            if old_forest_map[x][y]:
                forest_map[x][y] = cls.forest_tile_persists((x, y), old_forest_map, terrain)
            else:
                forest_map[x][y] = cls.forest_tile_grows((x, y), old_forest_map, terrain)

        return forest_map

    @classmethod
    def forest_tile_persists(cls, (x, y), forest_map, terrain):

        def is_forest((x, y)):
            return forest_map[x][y]

        persist_value = 10

        orth_adj = terrain.get_adj((x, y))
        for point in orth_adj:
            if is_forest(point):
                persist_value += 15

        diag_adj = cls.get_diagonal_adj((x, y), terrain)
        for point in diag_adj:
            if is_forest(point):
                persist_value += 10

        roll = randint(0, 99)

        return roll < persist_value

    @classmethod
    def forest_tile_grows(cls, (x, y), forest_map, terrain):

        def is_forest((x, y)):
            return forest_map[x][y]

        if terrain.get_tile((x, y)) not in cls.SEEDABLE:
            return False

        neighbours = 0

        orth_adj = terrain.get_adj((x, y))
        for point in orth_adj:
            if is_forest(point):
                neighbours += 1

        diag_adj = cls.get_diagonal_adj((x, y), terrain)
        for point in diag_adj:
            if is_forest(point):
                neighbours += .5

        return neighbours > 3

    @classmethod
    def get_diagonal_adj(cls, (x, y), terrain):

        adj = [(x-1, y-1), (x+1, y-1), (x-1, y+1), (x+1, y+1)]
        return filter(terrain.point_in_bounds, adj)

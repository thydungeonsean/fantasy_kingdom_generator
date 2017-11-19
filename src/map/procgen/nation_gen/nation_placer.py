from random import *
from src.constants import *
from nation_generator import NationGenerator
from src.nation.peoples.peoples import PEOPLES
from ..progress_bar import ProgressBar
from name_gen import NameGen

from src.map_object.army import Army


class NationPlacer(object):

    NUMBER_OF_NATIONS = 12
    NATION_SPACING = 15
    COLORS = PLAYER_COLORS[:]

    SETTLEMENT_BUFFER = 7
    MAX_START_SETTLEMENTS = 3

    NATION_SIZE = 30

    @classmethod
    def generate_nations(cls, state):

        cls.draw_progress_bar('PLACING NATIONS', .7)

        terrain = state.terrain_map

        valid_points = list(terrain.all_land)
        valid_points = filter(lambda x: cls.valid_capitol_point(terrain, x), valid_points)
        colors = list(cls.COLORS[:])
        shuffle(colors)

        peoples = cls.generate_world_population()

        placed = 0
        while placed < cls.NUMBER_OF_NATIONS and valid_points:

            point = choice(valid_points)
            valid_points = cls.space_from_new_nation(point, valid_points)

            nation = cls.generate_nation(state, point, colors, peoples)
            cls.place_nation(nation, point)
            placed += 1

        # grow nations influence to a certain point
        cls.draw_progress_bar('SPREADING INFLUENCE', .8)
        for i in range(cls.NATION_SIZE/2):
            state.nation_list.grow_nations(spread_amt=5)

        # place settlements
        cls.draw_progress_bar('PLACING SETTLEMENTS', .9)
        cls.place_settlements(state)

        cls.draw_progress_bar('WRAPPING UP', 1.0)
        for i in range(cls.NATION_SIZE / 2):
            state.nation_list.grow_nations(spread_amt=5)

        cls.generate_nation_names(state)

        # cls.add_armies(state)

    @classmethod
    def valid_capitol_point(cls, terrain, point):
        not_river = terrain.get_tile(point) != RIVER
        not_isolated = filter(lambda p: terrain.get_tile(p) != WATER, terrain.get_adj(point))
        return not_river and not_isolated

    @classmethod
    def space_from_new_nation(cls, (x, y), valid_points):

        too_close = set()
        for sx in range(-cls.NATION_SPACING+x, cls.NATION_SPACING+x):
            for sy in range(-cls.NATION_SPACING+y, cls.NATION_SPACING+y):
                too_close.add((sx, sy))

        return filter(lambda x: x not in too_close, valid_points)

    @classmethod
    def place_nation(cls, nation, point):

        nation.state.nation_list.add_nation(nation)

        nation.influence_point(point, 10)
        nation.update_borders()

    @classmethod
    def generate_nation(cls, state, point, colors, peoples):

        # create the capitol
        # find the preferred terrain
        # get the race/races
        # any other nation stuff
        # set color

        nation = NationGenerator.generate_nation(state, point, colors, peoples)

        # print nation.color
        # print nation.terrain_affinity.affinities

        return nation

    @classmethod
    def place_settlements(cls, state):

        for nation in state.nation_list.list_nations():

            cls.place_settlements_in_nation(nation)

    @classmethod
    def place_settlements_in_nation(cls, nation):

        nation_coords = nation.nation_coords.copy()

        def get_building_zone((x, y)):

            b = cls.SETTLEMENT_BUFFER

            zone = set([(zx, zy) for zx in range(x-b, x+b) for zy in range(y-b, y+b)])
            return zone

        for building in nation.settlements:

            building_zone = get_building_zone(building.coord)

            nation_coords = nation_coords.difference(building_zone)

        nation_coords = list(nation_coords)

        placed = 0
        while nation_coords and placed < cls.MAX_START_SETTLEMENTS:

            new_settlement = choice(nation_coords)
            zone = get_building_zone(new_settlement)

            nation.add_settlement(new_settlement)

            nation_coords = list(set(nation_coords).difference(zone))
            placed += 1

    @classmethod
    def generate_world_population(cls):

        peoples = []

        for p in PEOPLES:
            peoples.extend([p] * 3)  # 3 copies of each people in the overal peoples list

        return peoples

    @classmethod
    def draw_progress_bar(cls, message, progress):
        ProgressBar.draw_load_bar(message, progress)

    @classmethod
    def generate_nation_names(cls, state):

        names = set()

        for nation in state.nation_list.list_nations():

            nation_name = None
            while nation_name is None:
                nation_name = NameGen.generate_nation_name(nation)
                if nation_name in names:
                    nation_name = None
                else:
                    names.add(nation_name)
                    nation.set_name(nation_name)

    @classmethod
    def add_armies(cls, state):

        for nation in state.nation_list.list_nations():

            nation.military.add_army((0, 0))

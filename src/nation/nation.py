from src.constants import *
from random import randint
import math
from population import Population
from src.nation.buildings.settlement import Settlement


class Nation(object):

    VALID_TERRAIN = SWAMP, LOWLAND, FOREST, RIVER, ROUGH, HIGHLAND, MOUNTAIN, DESERT

    SPREAD_THRESHOLD = 5
    DEFAULT_MAX_INFLUENCE = 10

    MIN_ESTABLISH = 20
    MIN_SPREAD = 15

    def __init__(self, state):

        self.nation_coords = set()
        self.border_coords = set()
        self.spread_coords = set()
        self.needs_update = True
        self.new_points = []
        self.terrain_affinity = None
        self.max_influence = Nation.DEFAULT_MAX_INFLUENCE

        self.color = RED

        self.buildings = []
        self.population = Population(self)

        self.state = state

        # influence settings
        self.base_establish_rate = 100
        self.base_spread_rate = 90

    def set_terrain_affinity(self, affinity):
        self.terrain_affinity = affinity

    def set_color(self, color):
        self.color = color

    def initialize_terrain_influence(self):

        land = Nation.VALID_TERRAIN
        inf = {l: 10 for l in land}
        return inf

    @property
    def size(self):
        return len(self.nation_coords)

    # building methods
    def add_building(self, building):
        self.buildings.append(building)

    def add_settlement(self, point):
        settlement = Settlement(self, point)
        self.add_building(settlement)
        self.max_establish_point(point)

    @property
    def settlements(self):
        return list(filter(lambda b: b.building_class == 'settlement', self.buildings))

    def draw_buildings(self, surface):

        for building in filter(lambda x: self.object_visible(x), self.buildings):
            building.draw(surface)

    def object_visible(self, obj):
        return self.state.view.coord_in_view(obj.coord)

    # nation influence methods
    def claim_point(self, (x, y)):
        # add a point into the nation
        self.nation_coords.add((x, y))
        self.needs_update = True
        self.new_points.append((x, y))

    def lose_point(self, (x, y)):
        # remove a point from the nation
        self.nation_coords.remove((x, y))
        self.needs_update = True

    def establish_influence(self, point):  # increasing our influence points in a square we control

        terrain = self.state.terrain_map.get_tile(point)
        tries = self.terrain_affinity.get_affinity(terrain)

        influence = 0

        for i in range(tries):
            roll = randint(0, 99)
            # need to factor in distance from nearest settlement/capitol
            if roll < self.compute_establish_rate(point):

                influence += 1

        if influence > 0:
            self.influence_point(point, influence)

    def max_establish_point(self, point):
        self.influence_point(point, self.max_influence)

    def spread_influence(self, point, amt=1):
        # try to influence a point we don't control
        roll = randint(0, 99)
        if roll < self.compute_spread_rate(point):
            self.influence_point(point, amt)

    def influence_point(self, point, amt):
        if point in self.nation_coords:
            self.state.influence_map.increase_influence(self, point, amt)
        else:
            self.state.influence_map.spread_influence(self, point, amt)

    def point_is_valid(self, point):

        return self.state.terrain_map.get_tile(point) in Nation.VALID_TERRAIN

    def update_spread_coords(self):

        spread = set()

        able_to_spread = filter(lambda x: self.state.influence_map.get_influence(x) > Nation.SPREAD_THRESHOLD,
                                self.nation_coords)

        for point in able_to_spread:
            adj = self.state.terrain_map.get_adj(point)
            for a in adj:
                if a not in self.nation_coords and self.point_is_valid(a):
                    spread.add(a)

        self.spread_coords = spread

    def update_borders(self):

        if self.needs_update:

            self.state.color_overlay.update_squares(self.new_points)
            del self.new_points[:]

            self.needs_update = False

    def grow_nation(self, spread_amt=1):

        def coord_has_less_than_max_influence(point):
            return self.state.influence_map.get_influence(point) < self.max_influence

        points_to_influence = filter(coord_has_less_than_max_influence, self.nation_coords)

        for point in points_to_influence:
            self.establish_influence(point)

        self.update_spread_coords()

        for point in self.spread_coords:
            self.spread_influence(point, amt=spread_amt)

        self.update_borders()

    def get_nearest_settlement_value(self, (x, y)):

        coords = [n.coord for n in self.settlements]

        def dist_value((nx, ny)):
            vx = abs(x-nx)
            vy = abs(y-ny)
            #return int(math.hypot(vx, vy))
            return vx + vy

        return min([dist_value(c) for c in coords])  # nearest settlement value

    def compute_establish_rate(self, point):
        nearest_settlement = self.get_nearest_settlement_value(point)
        rate = max((self.base_establish_rate - nearest_settlement*3, Nation.MIN_ESTABLISH))
        return rate

    def compute_spread_rate(self, point):

        nearest_settlement = self.get_nearest_settlement_value(point)
        rate = max((self.base_spread_rate - nearest_settlement*3,  Nation.MIN_SPREAD))
        return rate

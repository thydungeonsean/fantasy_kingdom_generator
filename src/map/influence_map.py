from _map import _Map
from src.constants import *


class InfluenceMap(_Map):

    def __init__(self, terrain_map, state):
        w = terrain_map.w
        h = terrain_map.h
        _Map.__init__(self, w, h)

        self.state = state
        self.influence_map = self.initialize_influence_map()

    def initialize_influence_map(self):
        influence_map = [[0 for y in range(self.h)] for x in range(self.w)]

        for x, y in self.all_points:
            influence_map[x][y] = 0

        return influence_map

    def get_influence(self, (x, y)):
        return self.influence_map[x][y]

    def get_color(self, (x, y)):

        if self.influence_map[x][y] == 0:
            return None

        # else find the nation controlling this square and get it's color
        nation = self.find_owning_nation((x, y))
        return nation.color

    def find_owning_nation(self, point):
        return self.state.nation_list.get_nation_at_point(point, mode=1)

    def increase_influence(self, nation, (x, y), amt):

        self.influence_map[x][y] += amt
        self.influence_map[x][y] = min((nation.max_influence, self.influence_map[x][y]))

    def decrease_influence(self, nation, (x, y), amt):

        if amt >= self.influence_map[x][y]:
            self.change_owning_nation(nation, (x, y), amt)
        else:
            self.influence_map[x][y] -= amt

    def spread_influence(self, nation, (x, y), amt):

        if self.influence_map[x][y] == 0:
            nation.claim_point((x, y))
            self.increase_influence(nation, (x, y), amt)
        else:
            self.decrease_influence(nation, (x, y), amt)

    def change_owning_nation(self, nation, (x, y), amt):

        old_nation = self.find_owning_nation((x, y))
        old_nation.lose_point((x, y))

        amt += 1
        new_value = abs(self.influence_map[x][y] - amt)
        self.influence_map[x][y] = new_value

        nation.claim_point((x, y))



class NationList(object):

    def __init__(self, state):

        self.state = state
        self.nation_list = []

    def add_nation(self, nation):
        self.nation_list.append(nation)

    def remove_nation(self, nation):
        self.nation_list.remove(nation)

    def list_nations(self):

        for nation in self.nation_list:
            yield nation

    def grow_nations(self, spread_amt=1):

        nations = sorted(list(self.list_nations()), key=lambda x: x.size)

        for nation in nations:
            nation.grow_nation(spread_amt=spread_amt)
            for other_nation in self.list_nations():
                if other_nation != nation and other_nation.needs_update:
                    other_nation.update_borders()

    def draw(self, surface):

        for nation in self.list_nations():
            nation.draw_buildings(surface)

    def get_nation_at_point(self, point, mode=0):
        for nation in self.list_nations():
            if point in nation.nation_coords:
                return nation
        if mode == 0:
            return None
        else:
            raise Exception('if influence is not 0, there should be a controlling nation')
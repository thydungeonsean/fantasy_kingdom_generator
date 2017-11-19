from power import Power


class Raise(Power):

    def __init__(self):

        Power.__init__(self)

        self.valid_army_points = set()

    def click(self, point):
        if self.point_is_valid(point):
            self.place_army(point)
            # end turn

    def place_army(self, point):
        self.player_nation.military.add_army(point)

    def point_is_valid(self, point):

        return point in self.valid_army_points

    def deinit_functions(self):

        self.valid_army_points.clear()

    def init_functions(self):

        land = self.state.terrain_map.all_land
        valid = filter(lambda point: self.point_valid_for_army(point), land)

        self.valid_army_points.update(set(valid))

    def point_valid_for_army(self, point):

        # no nation, or this nation
        nation = self.state.nation_list.get_nation_at_point(point)
        valid_territory = nation == self.player_nation
        if not valid_territory:
            return False

        # not on top of settlement

        return True

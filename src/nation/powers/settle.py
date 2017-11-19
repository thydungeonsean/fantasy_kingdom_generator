from power import Power


class Settle(Power):

    def __init__(self):

        Power.__init__(self)
        self.valid_settle_points = set()

    def click(self, point):
        if self.point_is_valid(point):
            self.place_settlement(point)
            # end turn

    def place_settlement(self, point):

        self.player_nation.add_settlement(point)

    def point_is_valid(self, point):

        return point in self.valid_settle_points

    def deinit_functions(self):

        self.valid_settle_points.clear()

    def init_functions(self):

        land = self.state.terrain_map.buildable
        valid = filter(lambda point: self.point_valid_for_settlement(point), land)

        self.valid_settle_points.update(set(valid))

    def point_valid_for_settlement(self, point):

        # no nation, or this nation
        nation = self.state.nation_list.get_nation_at_point(point)
        valid_territory = nation == self.player_nation or nation is None
        if not valid_territory:
            return False

        # not too close to other settlements

        # within settlement range from borders

        return True


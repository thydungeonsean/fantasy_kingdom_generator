from maneuver import Maneuver


class Swap(Maneuver):

    def __init__(self):

        Maneuver.__init__(self)
        self.valid = False
        self.swaps = []

    def init(self):
        # highlight entire box if there are any valid swaps
        self.valid = self.find_swaps()
        if self.valid:
            self.highlight_battle_line()

    def deinit(self):
        self.valid = False
        del self.swaps[:]

    def find_swaps(self):

        battle_line = self.cursor.player_battle_line
        for y in range(7):

            a = (0, y)
            b = (1, y)

            units = filter(lambda u: u.coord in (a, b), battle_line.units)
            if len(units) == 2:
                self.swaps.append(units)

        return len(self.swaps) > 0

    def click(self, (mx, my)):

        cell = self.cursor.get_player_cell((mx, my))

        if self.valid and cell is not None:
            self.swap_lines()
            self.end_maneuver()

    def swap_lines(self):
        for a, b in self.swaps:
            a_coord = a.coord
            b_coord = b.coord
            self.move_unit(a, b_coord)
            self.move_unit(b, a_coord)

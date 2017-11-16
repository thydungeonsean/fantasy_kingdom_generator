from maneuver import Maneuver


class FallBack(Maneuver):

    def __init__(self):
        Maneuver.__init__(self)

    def init(self):
        for unit in self.battle_line.units:  # only valid targets
            self.highlight_unit(unit.coord)

    def click(self, (mx, my)):
        cell = self.cursor.get_player_cell((mx, my))
        unit = self.cursor.get_player_unit(cell)

        if unit is not None:
            self.fall_back(unit)
            self.end_maneuver()

    def fall_back(self, unit):
        print 'unit falls back'
        self.remove_unit(unit)
        # insert fade effect(unit)
        # something to remove a unit from battleline
        pass

from maneuver import Maneuver


class Rally(Maneuver):

    def __init__(self):

        Maneuver.__init__(self)

    def init(self):
        for unit in self.battle_line.units:  # only valid targets
            self.highlight_unit(unit.coord)

    def click(self, (mx, my)):
        cell = self.cursor.get_player_cell((mx, my))
        unit = self.cursor.get_player_unit(cell)

        if unit is not None:  # maybe you can only rally units with depleted morale too
            print unit
            self.rally(unit)
            self.end_maneuver()

    def rally(self, unit):
        print 'you have to make rally do something!'
        pass


from maneuver import Maneuver


class Push(Maneuver):

    def __init__(self):

        Maneuver.__init__(self)
        self.valid = False

    def init(self):

        self.valid = self.find_pushes()
        if self.valid:
            self.highlight_battle_line()

    def deinit(self):

        self.valid = False

    def find_pushes(self):

        battle_line = self.cursor.player_battle_line

        for y in range(7):

            cell = (1, y)
            push_cell = (0, y)

            unit = filter(lambda u: u.coord == cell, battle_line.units)
            blocker = filter(lambda u: u.coord == push_cell, battle_line.units)
            if len(unit) > 0 and len(blocker) == 0:
                return True

        return False

    def click(self, (mx, my)):

        cell = self.cursor.get_player_cell((mx, my))

        if self.valid and cell is not None:
            self.push_troops()
            self.end_maneuver()

    def push_troops(self):

        battle_line = self.cursor.player_battle_line

        for y in range(7):

            cell = (1, y)
            push_cell = (0, y)

            unit = filter(lambda u: u.coord == cell, battle_line.units)
            blocker = filter(lambda u: u.coord == push_cell, battle_line.units)
            if len(unit) > 0 and len(blocker) == 0:
                u = unit[0]
                self.move_unit(u, push_cell)

        print 'pooosh'

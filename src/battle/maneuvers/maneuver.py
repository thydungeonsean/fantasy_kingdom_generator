

class Maneuver(object):

    def __init__(self):

        self.cursor = None
        self.battle_line = None
        self.panel = None

    def bind(self, cursor, panel):
        self.cursor = cursor
        self.battle_line = self.cursor.player_battle_line
        self.panel = panel
        self.init()

    def free(self):
        self.cursor = None
        self.battle_line = None
        self.panel = None
        self.deinit()

    def init(self):
        pass

    def deinit(self):
        pass

    def click(self, (mx, my)):
        raise NotImplementedError

    def move_unit(self, unit, coord):
        self.battle_line.position_unit(unit, coord)

    def end_maneuver(self):
        self.panel.maneuver_complete()



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

    def init(self):
        pass

    def deinit(self):
        pass

    def click(self, (mx, my)):
        raise NotImplementedError

    def move_unit(self, unit, coord):
        self.battle_line.position_unit(unit, coord)

    def remove_unit(self, unit):
        self.battle_line.remove_unit(unit)

    def end_maneuver(self):
        self.panel.maneuver_complete()
        self.deinit()
        self.clear_highlights()

    def highlight_unit(self, cell):
        point = self.battle_line.get_image_coord(cell)
        self.cursor.state.highlighter.add_square(point)

    def highlight_battle_line(self):
        point = self.battle_line.coord
        self.cursor.state.highlighter.add_full(point)

    def highlight_selected_unit(self, cell):
        point = self.battle_line.get_image_coord(cell)
        self.cursor.state.highlighter.add_selected_square(point)

    def clear_highlights(self):

        self.cursor.state.highlighter.clear()

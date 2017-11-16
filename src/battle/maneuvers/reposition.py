from maneuver import Maneuver

class Reposition(Maneuver):

    SELECT_UNIT = 0
    SELECT_MOVE = 1

    def __init__(self):

        Maneuver.__init__(self)
        self.step = Reposition.SELECT_UNIT

        self.click_for_step = {
            Reposition.SELECT_UNIT: self.select_click,
            Reposition.SELECT_MOVE: self.select_move
        }

        self.clicked_cell = None
        self.selected_unit = None

    def init(self):
        self.init_select_step()

    def deinit(self):
        self.clicked_cell = None
        self.selected_unit = None
        self.step = Reposition.SELECT_UNIT

    def init_select_step(self):
        self.clear_highlights()
        for unit in self.battle_line.units:  # only valid targets
            self.highlight_unit(unit.coord)

    def init_move_step(self):
        self.clear_highlights()
        moves = self.battle_line.coord_list[:]
        moves.remove(self.selected_unit.coord)
        for point in moves:

            self.highlight_unit(point)
        self.highlight_selected_unit(self.selected_unit.coord)

    def click(self, (mx, my)):

        self.clicked_cell = self.cursor.get_player_cell((mx, my))

        self.click_for_step[self.step]()

    def select_click(self):
        unit = self.cursor.get_player_unit(self.clicked_cell)
        if unit is not None:
            self.step = Reposition.SELECT_MOVE
            self.selected_unit = unit
            self.init_move_step()

    def select_move(self):

        if self.clicked_cell is None:
            return

        displaced = None
        displaced_coord = None

        unit = self.cursor.get_player_unit(self.clicked_cell)
        if unit == self.selected_unit:  # deselect
            self.selected_unit = None
            self.step = Reposition.SELECT_UNIT
            self.init_select_step()
            return

        elif unit is not None:
            displaced = unit
            displaced_coord = self.selected_unit.coord

        if displaced is not None:
            self.move_unit(displaced, displaced_coord)

        self.move_unit(self.selected_unit, self.clicked_cell)

        self.end_maneuver()


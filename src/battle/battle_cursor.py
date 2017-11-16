from src.constants import *
import pygame


class BattleCursor(object):

    def __init__(self, state):

        self.state = state
        self.battle_lines = self.state.battle_lines.values()
        self.player_battle_line = self.state.battle_lines[self.state.player_side]

        self.selected_maneuver = None

    def set_maneuver(self, maneuver, panel):
        self.selected_maneuver = maneuver
        if self.selected_maneuver is not None:
            self.selected_maneuver.bind(self, panel)

    def clear_maneuver(self):
        if self.selected_maneuver is not None:
            self.selected_maneuver.clear_highlights()
            self.selected_maneuver.free()
            self.set_maneuver(None, None)

    def right_click(self):
        x, y = pygame.mouse.get_pos()
        unit = self.get_unit((x, y))
        # open unit panel

    def get_unit(self, (x, y)):
        for battle_line in self.battle_lines:
            if battle_line.point_is_over((x, y)):
                cell = self.get_relative_coord(battle_line, (x, y))
                return self.get_unit_at_cell(battle_line, cell)

    def get_player_unit(self, cell):
        if cell is not None:
            return self.get_unit_at_cell(self.player_battle_line, cell)
        return None

    def get_player_cell(self, (x, y)):
        if self.player_battle_line.point_is_over((x, y)):
            return self.get_relative_coord(self.player_battle_line, (x, y))
        return None

    def get_relative_coord(self, battle_line, (x, y)):

        bx, by = battle_line.coord

        rx = x - bx
        ry = y - by

        x = rx / UNITW
        y = ry / UNITH

        if battle_line.side == 'l':
            if x == 0:
                x = 1
            else:
                x = 0

        return x, y

    def get_unit_at_cell(self, battle_line, (x, y)):

        at_cell = list(filter(lambda u: u.coord == (x, y), battle_line.units))
        if not at_cell:
            return None
        elif len(at_cell) > 1:
            raise Exception('Why are there more than one unit in a cell!?!')
        else:
            return at_cell[0]

    def click_with_maneuver(self):

        mouse_pos = pygame.mouse.get_pos()
        self.selected_maneuver.click(mouse_pos)

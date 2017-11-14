from state_template import *
from src.constants import *


class BattleUITemplate(StateTemplate):

    menu_coord = SCREENW - Button.BUTTON_W - SCALE*10, SCALE*10

    def __init__(self, state, ui):

        StateTemplate.__init__(self, state, ui)

    def initialize_elements(self):

        menu_button = self.make_menu_button()

        return [menu_button]

    def make_menu_button(self):

        return self.make_button(BattleUITemplate.menu_coord, 'Menu', self.state.open_in_game_menu)

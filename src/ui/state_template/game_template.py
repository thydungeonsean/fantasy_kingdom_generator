from state_template import *
from src.constants import *


class GameUITemplate(StateTemplate):

    menu_coord = SCREENW - Button.BUTTON_W - SCALE*10, SCALE*10

    x = SCREENW - Button.BUTTON_W - SCALE * 10
    y = SCALE * 150
    button_space = Button.BUTTON_H + SCALE*5

    power_button_coords = {
        'Settle': (x, y),
        'Raise': (x, y+button_space)
    }

    power_button_text = {
        'Settle': 'Settle',
        'Raise': 'Raise Army'

    }

    def __init__(self, state, ui):

        def settle():
            print 'place holder'

        self.powers = {'Settle': settle, 'Raise': settle}

        StateTemplate.__init__(self, state, ui)

    def initialize_elements(self):

        menu_button = self.make_menu_button()

        settle_button = self.make_power_button('Settle')
        raise_button = self.make_power_button('Raise')

        return [menu_button, settle_button, raise_button]

    def make_menu_button(self):

        return self.make_button(GameUITemplate.menu_coord, 'Menu', self.state.open_in_game_menu)

    def make_power_button(self, key):
        cls = GameUITemplate
        return self.make_button(cls.power_button_coords[key], cls.power_button_text[key], self.powers[key])

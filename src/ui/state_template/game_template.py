from state_template import *
from src.constants import *


class GameUITemplate(StateTemplate):

    menu_coord = SCREENW - Button.BUTTON_W - SCALE*10, SCALE*10

    x = SCREENW - Button.BUTTON_W - SCALE * 10
    y = SCALE * 150
    button_space = Button.BUTTON_H + SCALE*5

    power_button_coords = {
        'Settle': (x, y),
        'Raise': (x, y+button_space),
        'Move': (x, y+button_space*2),
    }

    power_button_text = {
        'Settle': 'Settle',
        'Raise': 'Raise Army',
        'Move': 'Move Army',

    }

    def __init__(self, state, ui):

        self.power_buttons = {}
        StateTemplate.__init__(self, state, ui)

    def initialize_elements(self):

        menu_button = self.make_menu_button()

        power_buttons = [menu_button]
        for key in ('Settle', 'Raise', 'Move'):
            button = self.make_power_button(key)
            self.power_buttons[key] = button
            power_buttons.append(button)

        return power_buttons

    def make_menu_button(self):

        return self.make_button(GameUITemplate.menu_coord, 'Menu', self.state.open_in_game_menu)

    def make_power_button(self, key):
        cls = GameUITemplate
        return self.make_button(cls.power_button_coords[key], cls.power_button_text[key],
                                self.assign_power_select_function(key))

    def assign_power_select_function(self, key):

        def select_power():

            self.state.power_manager.select_power_button(key)

        return select_power

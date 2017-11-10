from state_template import *


class InGameMenuUI(StateTemplate):

    x = (SCREENW - Button.BUTTON_W) / 2
    y = (SCREENH - Button.BUTTON_H) / 2
    return_button_coord = x, y
    new_world_button_coord = x, y + Button.BUTTON_H + SCALE*5
    main_menu_button_coord = x, y + Button.BUTTON_H*2 + SCALE*5*2
    quit_button_coord = x, y + Button.BUTTON_H*3 + SCALE*5*3

    def __init__(self, state, ui):

        StateTemplate.__init__(self, state, ui)

    def initialize_elements(self):

        return_button = self.make_return_button()
        new_world_button = self.make_new_world_button()
        main_menu_button = self.make_main_menu_button()
        quit_button = self.make_quit_button()

        return [return_button, new_world_button, main_menu_button, quit_button]

    def make_return_button(self):

        return self.make_button(InGameMenuUI.return_button_coord, 'Return', self.state.return_to_game)

    def make_new_world_button(self):

        return self.make_button(InGameMenuUI.new_world_button_coord, 'New World', self.state.generate_new_world)

    def make_main_menu_button(self):

        return self.make_button(InGameMenuUI.main_menu_button_coord, 'Main Menu', self.state.return_to_main_menu)

    def make_quit_button(self):

        return self.make_button(InGameMenuUI.quit_button_coord, 'Quit', self.state.quit_program)

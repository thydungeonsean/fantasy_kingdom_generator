from src.ui.state_template.state_template import StateTemplate
from src.ui.button_panel import ButtonPanel
from battle_layout import *
from src.battle.maneuvers.maneuver_repo import maneuvers


class ManeuverChooser(StateTemplate):

    panel_coord = maneuver_panel['coord']

    x = panel_coord[0] + SCALE*5
    y = panel_coord[1] + SCALE*5
    button_space = Button.BUTTON_H + SCALE*5

    def __init__(self, state, ui, side):

        cls = ManeuverChooser

        self.available_maneuvers = ('swap', 'reposition', 'push', 'rally')

        self.maneuver_function = {m: self.create_maneuver_choose_func(m) for m in self.available_maneuvers}
        self.maneuver_function['pass'] = self.skip_maneuver

        self.side = side

        self.selection_table = {m: False for m in self.available_maneuvers}
        self.button_table = {}

        StateTemplate.__init__(self, state, ui)

    def get_button_coord(self, i):
        cls = ManeuverChooser
        return cls.x, cls.y + cls.button_space * (i + 1)

    def initialize_elements(self):

        cls = ManeuverChooser

        buttons = []

        x, y = cls.panel_coord
        if self.side == 'r':
            x += disposition_panel['right']
        panel = ButtonPanel((x, y), 'Choose Maneuver', num_buttons=len(self.available_maneuvers)+1)
        buttons.append(panel)

        i = 0
        keys = self.available_maneuvers[:] + ('pass',)

        for m in keys:

            x, y = self.get_button_coord(i)
            if self.side == 'r':
                x += disposition_panel['right']

            button = self.make_button((x, y), m.capitalize(), self.maneuver_function[m])
            buttons.append(button)
            self.button_table[m] = button
            i += 1

        return buttons

    def deselect_button(self, m):
        self.selection_table[m] = False
        self.button_table[m].normal()
        self.state.cursor.clear_maneuver()

    def select_button(self, m):
        self.selection_table[m] = True
        self.button_table[m].highlight()
        maneuver_object = maneuvers[m]
        self.state.cursor.set_maneuver(maneuver_object, self)

    def select_maneuver_func(self, maneuver):
        # select the maneuver
        # bind maneuver to the cursor
        if self.selection_table[maneuver]:
            self.deselect_button(maneuver)
        else:
            for m in self.available_maneuvers:
                self.deselect_button(m)

            self.select_button(maneuver)

    def create_maneuver_choose_func(self, key):

        def func():
            self.select_maneuver_func(key)

        return func

    def skip_maneuver(self):
        self.maneuver_complete()

    def maneuver_complete(self):
        self.state.turn_structure.player_chose_maneuver()
        self.remove_from_state()

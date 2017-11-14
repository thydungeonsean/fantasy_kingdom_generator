from src.ui.state_template.state_template import StateTemplate
from src.ui.button_panel import ButtonPanel
from battle_layout import *


class DispositionChooser(StateTemplate):

    CHARGING = 0
    DEFENDING = 1
    ADVANCING = 2

    dispositions = (CHARGING, DEFENDING, ADVANCING)

    panel_coord = disposition_panel['coord']

    x = panel_coord[0] + SCALE*5
    y = panel_coord[1] + SCALE*5
    button_space = Button.BUTTON_H + SCALE*5

    disp_button_coords = {
        CHARGING: (x, y+button_space),
        DEFENDING: (x, y+button_space*2),
        ADVANCING: (x, y+button_space*3),
    }

    disp_button_text = {
        CHARGING: 'Charging',
        DEFENDING: 'Defending',
        ADVANCING: 'Advancing',
    }

    def __init__(self, state, ui, side):

        cls = DispositionChooser

        self.select_disposition = {
            cls.CHARGING: self.select_charging,
            cls.DEFENDING: self.select_defending,
            cls.ADVANCING: self.select_advancing,
        }

        self.side = side

        StateTemplate.__init__(self, state, ui)

    def initialize_elements(self):

        cls = DispositionChooser

        buttons = []

        x, y = cls.panel_coord
        if self.side == 'r':
            x += disposition_panel['right']
        panel = ButtonPanel((x, y), 'Choose Disposition')
        buttons.append(panel)

        for d in cls.dispositions:

            x, y = cls.disp_button_coords[d]
            if self.side == 'r':
                x += disposition_panel['right']

            button = self.make_button((x, y), cls.disp_button_text[d], self.select_disposition[d])
            buttons.append(button)

        return buttons

    def select_disposition_func(self, disposition):
        battle_line = self.state.get_battle_line_by_key(self.state.player_controlled)
        battle_line.set_disposition(disposition)
        self.state.panel.update()
        self.state.turn_structure.player_chose_disposition()
        self.remove_from_state()

    def select_charging(self):
        self.select_disposition_func(DispositionChooser.CHARGING)

    def select_defending(self):
        self.select_disposition_func(DispositionChooser.DEFENDING)

    def select_advancing(self):
        self.select_disposition_func(DispositionChooser.ADVANCING)

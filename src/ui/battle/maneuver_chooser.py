from src.ui.state_template.state_template import StateTemplate
from src.ui.button_panel import ButtonPanel
from battle_layout import *


class ManeuverChooser(StateTemplate):

    panel_coord = maneuver_panel['coord']

    x = panel_coord[0] + SCALE*5
    y = panel_coord[1] + SCALE*5
    button_space = Button.BUTTON_H + SCALE*5

    def __init__(self, state, ui, side):

        cls = ManeuverChooser

        self.available_maneuvers = ('swap', 'move', 'push')

        def standin():
            print 'hi'

        self.select_maneuver = {'swap': standin,
                                'move': standin,
                                'push': standin
                                }

        self.side = side

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
        panel = ButtonPanel((x, y), 'Choose Maneuver')
        buttons.append(panel)

        i = 0
        for m in self.available_maneuvers:

            x, y = self.get_button_coord(i)
            if self.side == 'r':
                x += disposition_panel['right']

            button = self.make_button((x, y), m.capitalize(), self.select_maneuver[m])
            buttons.append(button)
            i += 1

        return buttons

    def select_maneuver_func(self, disposition):
        # select the maneuver
        # bind maneuver to the cursor
        pass


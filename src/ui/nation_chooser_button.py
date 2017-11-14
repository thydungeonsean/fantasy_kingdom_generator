from button import Button
from src.constants import SCALE
from nation_display import NationDisplay


class NationChooserButton(Button):

    coord = NationDisplay.coord[0], NationDisplay.coord[0] + SCALE*5 + NationDisplay.h

    def __init__(self, nation):

        Button.__init__(self, NationChooserButton.coord, 'Select Nation')
        self.nation = nation
        self.state = nation.state

        self.on_click = self.choose_nation

    def choose_nation(self):

        self.state.choose_nation(self.nation)

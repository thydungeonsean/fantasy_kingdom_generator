from ..button import Button
from battle_layout import engage_coord


class EngageButton(Button):

    coord = engage_coord

    def __init__(self, turn_tracker, ui):

        Button.__init__(self, EngageButton.coord, 'Engage')
        self.ui = ui
        self.turn_tracker = turn_tracker

    def on_click(self):
        print 'engage!'
        self.ui.remove_element(self)
        self.turn_tracker.start_new_turn()


from ..button import Button
from battle_layout import engage_coord


class EngageButton(Button):

    coord = engage_coord

    def __init__(self, turn_tracker, ui):

        Button.__init__(self, EngageButton.coord, 'Engage')
        self.ui = ui
        self.turn_tracker = turn_tracker

    def on_click(self):
        print 'engage! ... needs to trigger the battle calculator and run animations and such'
        self.ui.state.trigger_engagement()
        self.ui.remove_element(self)
        self.turn_tracker.start_new_turn()



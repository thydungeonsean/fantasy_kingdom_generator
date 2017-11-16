from src.ui.battle.disposition_chooser import DispositionChooser
from src.ui.battle.maneuver_chooser import ManeuverChooser
from src.ui.battle.engage_button import EngageButton


class TurnStructure(object):

    CHOOSE_DISPOSITION = 0
    CHOOSE_MANEUVER = 1
    ENGAGE = 2

    def __init__(self, state):

        self.state = state
        self.player = state.player_controlled
        self.ai = state.ai_controlled

        self.stage = TurnStructure.CHOOSE_DISPOSITION

    def start_new_turn(self):
        print 'here again'
        self.stage = TurnStructure.CHOOSE_DISPOSITION
        DispositionChooser(self.state, self.state.ui, self.state.sides[self.player]).add_to_state()

    def player_chose_disposition(self):

        self.stage = TurnStructure.CHOOSE_MANEUVER
        ManeuverChooser(self.state, self.state.ui, self.state.sides[self.player]).add_to_state()

    def player_chose_maneuver(self):

        self.stage = TurnStructure.ENGAGE
        print 'engage part!!!'
        # open_engage controls
        self.state.ui.add_element(EngageButton(self, self.state.ui))

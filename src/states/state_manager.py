from game_state import GameState
from main_menu_state import MainMenuState
from in_game_menu import InGameMenuState
from battle_state import BattleState


class StateManager(object):

    def __init__(self):

        self.current_state = MainMenuState(self)

    def main(self):

        while self.current_state is not None:
            complete = self.current_state.main()
            if complete:
                next_state_key = self.current_state.get_next_state()
                self.current_state = self.load_next_state(next_state_key)

    def load_next_state(self, next_state):
        if next_state == 'exit':
            return None
        else:
            return next_state

    def load_new_game(self):
        state = GameState(self)
        return state

    def load_main_menu(self):
        state = MainMenuState(self)
        return state

    def load_in_game_menu(self, game):
        state = InGameMenuState(self, game)
        return state

    def start_battle(self, game, attacker, defender):
        state = BattleState(self, game, attacker, defender)
        return state

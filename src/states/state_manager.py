from game_state import GameState


class StateManager(object):

    def __init__(self):

        self.current_state = GameState(self)

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

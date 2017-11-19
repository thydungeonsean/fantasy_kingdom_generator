

class Power(object):

    def __init__(self):

        self.state = None
        self.player_nation = None

    def bind(self, state):

        self.state = state
        self.player_nation = state.player_nation
        self.init_functions()

    def free(self):

        self.state = None
        self.player_nation = None
        self.deinit_functions()

    def init_functions(self):
        pass

    def deinit_functions(self):
        pass

    def click(self, point):

        raise NotImplementedError

    def point_is_valid(self, point):
        return True

from power import Power


class Move(Power):

    SELECT = 0
    MOVE = 1

    def __init__(self):

        Power.__init__(self)

        self.stage = Move.SELECT

    def init_functions(self):
        self.stage = Move.SELECT
        self.selected_army = None

    def deinit_functions(self):
        self.stage = Move.SELECT
        self.selected_army = None

    def click(self, point):
        pass

    def point_is_valid(self, point):
        return True




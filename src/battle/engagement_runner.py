

class EngagementRunner(object):

    def __init__(self, state):

        self.state = state
        self.attacker = self.get_battle_line('l')
        self.defender = self.get_battle_line('r')

    def get_battle_line(self, side):

        return self.state.battle_lines[side]

    def run_engagement(self):

        self.run_line(self.attacker, self.defender)
        self.run_line(self.defender, self.attacker)

    def run_line(self, battle_line, target_line):

        pass


from random import *
from src.map_object.unit_stat import UnitStats


class EngagementRunner(object):

    CHARGING = 0
    DEFENDING = 1
    ADVANCING = 2

    disp_dict = {CHARGING: UnitStats.CHARGING, DEFENDING: UnitStats.DEFENDING, ADVANCING: UnitStats.ADVANCING}

    HIT_RATE = 4

    def __init__(self, state):

        self.state = state
        self.attacker = self.get_battle_line('l')
        self.defender = self.get_battle_line('r')

        self.battle_effects = []

    def get_battle_line(self, side):

        return self.state.battle_lines[side]

    def run_engagement(self):

        self.run_line(self.attacker, self.defender)
        self.run_line(self.defender, self.attacker)

        self.apply_battle_effects()
        del self.battle_effects[:]

    def run_line(self, battle_line, target_line):

        for coord in battle_line.coord_list:

            unit = battle_line.get_unit_at_coord(coord)
            if unit is not None and self.unit_can_attack(unit):
                self.calculate_unit_attack(unit, battle_line, target_line)

    def apply_battle_effects(self):

        for target, hits, row in self.battle_effects:
            target.take_hits(hits, row)

    def unit_can_attack(self, unit):

        x, y = unit.coord
        return x == 0  # also put in stuff to allow special units to attack from back row

    def calculate_unit_attack(self, unit, battle_line, target_line):

        attack_value = self.get_attack_value(unit, battle_line)

        hits = self.calculate_hits(attack_value)

        print '%s %d rolled: %d hit' % (unit.unit_key, attack_value, hits)

        unit_row = unit.coord[1]
        if hits > 0:
            self.battle_effects.append((target_line, hits, unit_row))

    def get_attack_value(self, unit, battle_line):
        disp = battle_line.disposition
        return unit.stats.get(EngagementRunner.disp_dict[disp])

    def calculate_hits(self, attack_value):

        hits = 0
        for i in range(attack_value):

            roll = randint(1, 10)
            if roll >= EngagementRunner.HIT_RATE:
                hits += 1

        return hits



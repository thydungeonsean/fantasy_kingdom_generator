from unit_stat_table import *


class UnitStats(object):

    CHARGING = CHARGING
    ADVANCING = ADVANCING
    DEFENDING = DEFENDING
    MORALE = MORALE

    def __init__(self, unit):

        self.unit = unit
        self.key = unit.unit_key

        self.stats = {}

        self.load_stats()
        self.apply_nation_qualities()

        self.stats['max_morale'] = self.stats['morale']

    def load_stats(self):

        if specific_types.get(self.key, None) is not None:
            print specific_types.get(self.key)
            self.compile_stats(specific_types.get(self.key))
            return

        key_sequence = self.key.split('_')
        if len(key_sequence) > 1:
            stock = key_sequence[0]
            gen_type = key_sequence[-1]
            self.compile_stats(gen_types[gen_type])
            self.apply_stock_qualities(stock)
        else:
            self.compile_stats(default_stats)

    def compile_stats(self, profile):

        for k, v in profile.stats.iteritems():
            self.stats[k] = v

    def apply_stock_qualities(self, key):
        stock = stock_types[key]
        stock.apply_profile(self.stats)

    def apply_nation_qualities(self):
        pass

    def get(self, key):
        return self.stats.get(key, None)

    def take_hits(self, hits):

        self.stats['morale'] -= hits

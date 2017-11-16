

# stats
# charge dice, advance dice, defend dice
# morale
# special abilities

CHARGING = 'charge'
ADVANCING = 'advance'
DEFENDING = 'defend'
MORALE = 'morale'


class StatProfile(object):

    default = {CHARGING: 0, ADVANCING: 0, DEFENDING: 0, MORALE: 0}
    numeric = (CHARGING, ADVANCING, DEFENDING, MORALE)

    def __init__(self, **kwargs):

        self.stats = {}

        for stat in StatProfile.default.keys():
            if kwargs.get(stat, None) is not None:
                self.stats[stat] = kwargs.get(stat)
            else:
                self.stats[stat] = StatProfile.default.get(stat)

    def apply_profile(self, target_dict):

        for k in StatProfile.numeric:
            target_dict[k] += self.stats[k]

# stock types
stock_types = {
    'centaur': StatProfile(charge=1),
    'naga': StatProfile(advance=1),
    'ogre': StatProfile(defend=1),
    'goblin': StatProfile(),
    'kobold': StatProfile(),
    'avian': StatProfile(advance=1),
    'dark': StatProfile(advance=1),
    'skeleton': StatProfile(),
    'ratling': StatProfile(),
    'orc': StatProfile(charge=1),
    'gnome': StatProfile(morale=1),
    'fey': StatProfile(defend=1),
    'dwarf': StatProfile(advance=1),
    'halfling': StatProfile(morale=1),
    'elf': StatProfile(defend=1),
    'barbarian': StatProfile(charge=1),
    'knight': StatProfile(morale=1),
    'citizen': StatProfile(advance=1),
    'nomad': StatProfile(defend=1),
}

# generic types
gen_types = {
    'warrior': StatProfile(charge=2, advance=1, morale=3),
    'archer': StatProfile(advance=1, defend=3, morale=2),
    'knight': StatProfile(charge=3, advance=2, defend=1, morale=4),
    'soldier': StatProfile(charge=1, advance=2, defend=2, morale=2),
    'chief': StatProfile(charge=2, advance=1, defend=4, morale=5),
    'mage': StatProfile(defend=8),
    'grunt': StatProfile(charge=1, advance=1, morale=3),
    'scout': StatProfile(advance=2),
    'berserker': StatProfile(charge=3, morale=2),
    'magician': StatProfile(defend=6, morale=3),
    'magi': StatProfile(charge=1, advance=1, defend=4, morale=4),
    'enchanter': StatProfile(advance=2, defend=3),
    'champion': StatProfile(charge=2, advance=2, defend=2, morale=4),
    'slinger': StatProfile(charge=1, defend=2, morale=2),
    'ranger': StatProfile(advance=1, defend=4, morale=3),
    'druid': StatProfile(defend=7, morale=3),
    'cavalry': StatProfile(charge=3, advance=1, morale=2),
    'templar': StatProfile(charge=1, advance=2, defend=2, morale=3),
    'legionary': StatProfile(advance=4, defend=3, morale=3),
    'acolyte': StatProfile(defend=5, morale=2),
    'axe': StatProfile(advance=2, defend=2, morale=3),
    'spear': StatProfile(charge=2, defend=2, morale=2),
}

# spider, zombie, necromancer, gnome, minotaur, treant, fey
specific_types = {

}

default_stats = StatProfile()



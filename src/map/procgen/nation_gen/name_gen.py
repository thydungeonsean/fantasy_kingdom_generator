from random import *


class NameGen(object):

    vowel_start_chance = 35

    simple_consonant_start = (
        'k', 'c', 'd', 'dh', 'g', 'b', 'j', 'kh', 'z'

    )

    simple_syllable_body = (
        'ar', 'al', 'agh', 'or', 'on', 'an', 'ara', 'ond', 'end', 'and', 'ir', 'or', 'ur', 'oor'
    )

    pair_end = ('heim', 'lund', 'land', 'ania', 'ia', 'or', 'oria', 'ar', 'ina', 'ena')

    @classmethod
    def pair_name(cls):

        start = cls.get_simple_syllable()
        end = choice(cls.pair_end)

        pair_name = ''.join((start, end)).capitalize()
        return pair_name

    @classmethod
    def get_simple_syllable(cls):
        if randint(0, 99) < cls.vowel_start_chance:
            start = ''
        else:
            start = choice(cls.simple_consonant_start)

        mid = choice(cls.simple_syllable_body)

        return ''.join((start, mid))

    @classmethod
    def generate_nation_name(cls, nation):

        return cls.pair_name()

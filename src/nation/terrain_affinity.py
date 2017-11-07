from src.constants import *


class TerrainAffinity(object):

    str_to_code = {'lowland': LOWLAND, 'highland': HIGHLAND, 'swamp': SWAMP, 'desert': DESERT,
                   'forest': FOREST, 'rough': ROUGH, 'river': RIVER, 'mountain': MOUNTAIN}

    code_to_str = {v: k for k, v in str_to_code.iteritems()}

    keys = str_to_code.keys()
    DEFAULT = 1

    def __init__(self, **kwargs):

        self.affinities = {}

        for key in TerrainAffinity.keys:
            self.affinities[key] = kwargs.get(key, TerrainAffinity.DEFAULT)

    def get_affinity(self, terrain):

        return self.affinities[self.decode_terrain(terrain)]

    def decode_terrain(self, terrain):
        return TerrainAffinity.code_to_str[terrain]

    def get_main_affinity(self):

        terrain = None
        affinity = 0
        for k, v in self.affinities.iteritems():

            if v > affinity:
                affinity = v
                terrain = k

        return terrain



class AutomataTerrainGenerator(object):

    @classmethod
    def create_new_automata_map(cls, terrain):

        w = terrain.w
        h = terrain.h
        automata_map = [[False for y in range(h)] for x in range(w)]
        return automata_map

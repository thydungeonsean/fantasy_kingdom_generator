from src.image.map_object_image import MapObjectImage
from src.constants import ARMY
from unit import Unit


class Army(object):

    MAX_SIZE = 14

    def __init__(self, nation, coord, points=10):

        self.nation = nation
        self.state = nation.state
        self.unit_list = self.initialize_unit_list(points)
        self.color = self.nation.color

        self.army_image = MapObjectImage(ARMY, self, self.nation.color)

        self.coord = coord  # coord on world map

    def initialize_unit_list(self, points):

        unit_dict = {}
        # fill with a semi random sampling of this nations available units
        # use points to determine when it is done
        # each item in list is a tuple
        # (str unit_key, int count)

        count = 0

        while points > 0 and count < Army.MAX_SIZE:
            unit = self.nation.population.get_random_troop()

            if unit_dict.get(unit, None) is None:
                unit_dict[unit] = 1
            else:
                unit_dict[unit] += 1

            points -= 1  # get_unit_points(unit)

            count += 1

        unit_list = [(u, c) for u, c in unit_dict.iteritems()]

        return unit_list

    def draw(self, surface):
        self.army_image.draw(surface)

    def move(self, new_coord):
        self.coord = new_coord

    def build_army(self):
        # goes through each key, count pair in unit list and builds unit objects
        # returns list of objects
        unit_object_list = []

        for unit_key, count in self.unit_list:
            for i in range(count):
                unit_object_list.append(Unit(self, unit_key))

        return unit_object_list

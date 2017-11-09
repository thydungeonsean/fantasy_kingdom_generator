from src.image.unit_image import UnitImage
from people_units import unit_associations


class People(object):

    def __init__(self, name, nation):

        self.name = name
        self.nation = nation
        self.color = nation.color
        self.base_affinity = self.get_people_affinity()
        self.nation_affinity = nation.terrain_affinity.get_main_affinity()

        self.unit_pool = self.set_unit_pool(name)
        self.image_cache = self.set_image_cache()

    def set_unit_pool(self, name):

        return unit_associations[name]

    def set_image_cache(self):

        cache = {}
        for unit in self.unit_pool:

            cache[unit] = UnitImage(unit, self.color)

        return cache

    def get_troop_image(self, key):
        return self.image_cache[key]

    def get_people_affinity(self):

        return 1

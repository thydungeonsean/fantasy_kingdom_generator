from src.image.unit_image import UnitImage
from people_units import unit_associations


class People(object):

    @classmethod
    def elf(cls, nation):

        return cls('elf', nation)

    @classmethod
    def centaur(cls, nation):

        return cls('centaur', nation)

    @classmethod
    def naga(cls, nation):
        return cls('naga', nation)

    @classmethod
    def ogre(cls, nation):
        return cls('ogre', nation)

    @classmethod
    def goblin(cls, nation):
        return cls('goblin', nation)

    @classmethod
    def kobold(cls, nation):
        return cls('kobold', nation)

    @classmethod
    def avian(cls, nation):
        return cls('avian', nation)

    @classmethod
    def dark_elf(cls, nation):
        return cls('dark_elf', nation)

    @classmethod
    def undead(cls, nation):
        return cls('undead', nation)

    @classmethod
    def knight(cls, nation):
        return cls('knight', nation)

    def __init__(self, name, nation):

        self.name = name
        self.nation = nation
        self.color = nation.color
        self.base_affinity = self.get_people_affinity()
        self.nation_affinity = nation.terrain_affinity.get_main_affinity()
        print self.nation_affinity

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

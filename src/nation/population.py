from random import choice


class Population(object):

    def __init__(self, nation):

        self.nation = nation
        self.image_cache = {}
        self.peoples = []
        self.troop_list = []

    def add_people(self, people):
        self.peoples.append(people)
        self.link_images(people)
        self.add_troops(people)
        print self.troop_list

    def link_images(self, people):

        for k, v in people.image_cache.iteritems():
            self.image_cache[k] = v

    def add_troops(self, people):
        map(lambda x: self.troop_list.append(x), people.unit_pool)

    def get_image(self, key):
        return self.image_cache.get(key)

    def get_random_troop(self):

        return choice(self.troop_list)

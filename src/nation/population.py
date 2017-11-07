

class Population(object):

    def __init__(self, nation):

        self.nation = nation
        self.peoples = []

    def add_people(self, people):
        self.peoples.append(people)

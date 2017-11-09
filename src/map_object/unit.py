

class Unit(object):

    def __init__(self, army, unit_key):

        self.army = army
        self.unit_key = unit_key

        self.image = self.get_reference_to_image()

    def get_reference_to_image(self):

        return self.army.nation.population.get_image(self.unit_key)

    def run(self):
        pass

    def draw(self, surface, frame=0):
        self.image.draw(surface, frame)

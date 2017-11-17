from unit_stat import UnitStats


class Unit(object):

    def __init__(self, army, unit_key):

        self.army = army
        self.unit_key = unit_key
        self.coord = (0, 0)
        self.image_coord = (0, 0)

        self.stats = UnitStats(self)
        self.image = self.get_reference_to_image()

    def get_reference_to_image(self):

        return self.army.nation.population.get_image(self.unit_key)

    def run(self):
        pass

    def draw(self, surface, frame, facing):

        image_key = '_'.join((facing, frame))
        self.image.draw_animated(surface, self.image_coord, image_key)

    def set_coord(self, coord):
        self.coord = coord

    def set_image_coord(self, coord):
        self.image_coord = coord

    def take_hits(self, hits):

        self.stats.take_hits(hits)
        # self.flash()

    @property
    def dead(self):
        return self.stats.get('morale') <= 0

    @property
    def wavering(self):
        return not self.dead and self.stats.get('morale') < self.stats.get('max_morale')

    def flash(self):
        pass


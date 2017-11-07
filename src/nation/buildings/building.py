from src.image.building_image import BuildingImage


class Building(object):

    def __init__(self, nation, coord, building_class, image_key=None):

        self.nation = nation
        self.state = nation.state
        self.coord = coord
        self.building_class = building_class

        self.building_image = BuildingImage(image_key, self.nation.color, self)

    def draw(self, surface):

        self.building_image.draw(surface)

from src.image.map_object_image import MapObjectImage


class Building(object):

    def __init__(self, nation, coord, building_class, image_key=None):

        self.nation = nation
        self.state = nation.state
        self.coord = coord
        self.building_class = building_class

        self.building_image = MapObjectImage(image_key, self, self.nation.color)

    def draw(self, surface):

        self.building_image.draw(surface)

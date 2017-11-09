from image import Image
from src.constants import TILEW, TILEH


class MapObjectImage(Image):

    BASE_COLOR = (125, 125, 125)

    def __init__(self, key, owner, color):

        self.owner = owner
        Image.__init__(self, key, transparent=True)

        self.color = MapObjectImage.BASE_COLOR
        self.recolor_image(color)

    def set_position(self):
        self.coord = self.get_relative_coord()

    def get_relative_coord(self):

        ax, ay = self.owner.coord
        vx, vy = self.owner.state.view.coord

        return (ax - vx) * TILEW, (ay - vy) * TILEH

    def draw(self, surface):

        self.set_position()
        surface.blit(self.surface, self.coord)

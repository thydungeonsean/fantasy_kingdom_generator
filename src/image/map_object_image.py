from image import Image
from src.constants import TILEW, TILEH


class MapObjectImage(Image):

    def __init__(self, key, owner):

        self.owner = owner
        Image.__init__(self, key, transparent=True)

    def set_position(self):
        self.coord = self.get_relative_coord()

    def get_relative_coord(self):

        ax, ay = self.owner.coord
        vx, vy = self.owner.state.view.coord

        return (ax - vx) * TILEW, (ay - vy) * TILEH

    def draw(self, surface):

        self.set_position()
        surface.blit(self.surface, self.coord)
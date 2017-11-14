from image import Image
import tile_key
from src.constants import *
import pygame


class UnitImage(Image):

    BASE_COLOR = BLACK

    def __init__(self, key, color):

        Image.__init__(self, key, transparent=True)
        self.frames = self.set_frames(key)

        self.color = UnitImage.BASE_COLOR
        self.recolor_image(color)

    def get_tile(self, key):
        return tile_key.units[key]

    def get_tile_rect(self):
        return tile_key.unit_rect

    def get_tile_sheet(self):
        return tile_key.load_unit_sheet()

    def get_tile_dim(self):
        return UNITW, UNITH

    def get_base_tile_dim(self):
        return BASE_UNIT_W, BASE_UNIT_H

    def set_frames(self, key):

        frames = {
                  'r_a': self.surface,
                  'r_b': self.initialize_surface(self._b_frame_key(key), transparent=True),
                  'l_a': self.flip(self.initialize_surface(key, transparent=True)),
                  'l_b': self.flip(self.initialize_surface(self._b_frame_key(key), transparent=True))
                  }
        return frames

    def _b_frame_key(self, key):

        return ''.join((key, '_b'))

    def recolor_image(self, color):

        for image in self.frames.values():
            pix_array = pygame.PixelArray(image)
            pix_array.replace(self.color, color)

        self.color = color

    def set_position(self, pos):
        self.coord = pos

    def draw_animated(self, surface, coord, frame):
        image = self.frames[frame]
        surface.blit(image, coord)

    def flip(self, surface):

        return pygame.transform.flip(surface, True, False)

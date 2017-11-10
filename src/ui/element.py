import pygame
from src.constants import *


class Element(object):

    def __init__(self, coord, w, h):

        self.coord = coord
        self.w = w
        self.h = h

        self.ui = None

        self.surface = self.initialize_surface()

    def initialize_surface(self):

        image = pygame.Surface((self.w, self.h)).convert()
        image.fill(BLACK)

        return image

    def set_ui(self, ui):
        self.ui = ui

    @property
    def x(self):
        return self.coord[0]

    @property
    def y(self):
        return self.coord[1]

    def point_is_over(self, (x, y)):
        return self.x <= x < self.x + self.w and self.y <= y < self.y + self.h

    def draw(self, surface):

        surface.blit(self.surface, self.coord)

    def run(self):
        pass

    def click(self, point):
        return False

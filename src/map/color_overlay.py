import pygame
from src.constants import *
from random import choice


class ColorOverlay(object):

    TRANSPARENCY = 100

    def __init__(self, influence_map):

        self.influence_map = influence_map
        self.w = self.influence_map.w
        self.h = self.influence_map.h

        self.view = None
        self.view_rect = pygame.Rect((0, 0), (SCREENW, SCREENH))

        self.color_square = pygame.Surface((TILEW, TILEH)).convert()

        self.surface = self.initialize_surface()

        self.update_point_set = set()

        self.render_all()

    def initialize_surface(self):

        surface = pygame.Surface((self.w * TILEW, self.h * TILEH)).convert()

        surface.fill(BLACK)
        surface.set_colorkey(BLACK)
        surface.set_alpha(ColorOverlay.TRANSPARENCY)

        return surface

    def set_view(self, view):
        self.view = view

    def draw(self, surface):

        if self.view is None:
            surface.blit(self.surface, (0, 0))
            return

        vx, vy = self.view.coord
        self.view_rect.topleft = vx * TILEW, vy * TILEH
        surface.blit(self.surface, (0, 0), self.view_rect)

    def render_all(self):

        for x, y in self.influence_map.all_points:
            self.update_square((x, y))

    def update_square(self, (x, y)):

        color = self.influence_map.get_color((x, y))
        if color is None:
            return

        # color = choice((RED, BLUE, YELLOW))
        self.color_square.fill(color)

        px = x * TILEW
        py = y * TILEW

        self.surface.blit(self.color_square, (px, py))

    def update_squares(self, update_list):

        for point in update_list:
            self.update_square(point)


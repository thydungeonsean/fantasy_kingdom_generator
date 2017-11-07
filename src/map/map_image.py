from src.constants import *
from src.image.image_cache import ImageCache
import pygame


class MapImage(object):

    SHADE_LEVEL = 200
    LOWER_SHADE_LEVEL = 125

    THUMB_W = 5
    THUMB_H = 5

    def __init__(self, terrain_map, height_map, state=None):

        self.terrain_map = terrain_map
        self.height_map = height_map
        self.state = state

        self.view = None

        self.view_rect = pygame.Rect((0, 0), (SCREENW, SCREENH))

        self.shade = None
        self.thumbnail = self.initialize_thumbnail()
        self.base_map_surface = self.initialize_surface()
        self.render_base_map()
        self.compiled_image = self.initialize_surface()

    def set_view(self, view):
        self.view = view

    def initialize_surface(self):

        surface = pygame.Surface((self.terrain_map.w * TILEW, self.terrain_map.h * TILEH)).convert()

        surface.fill(BLACK)

        return surface

    def initialize_thumbnail(self):

        tw = MapImage.THUMB_W
        th = MapImage.THUMB_H
        thumbnail = pygame.Surface((self.terrain_map.w * tw, self.terrain_map.h * th)).convert()

        self.initialize_shade(tw, th)
        cache = ImageCache.get_instance()

        for x, y in self.terrain_map.all_points:

            terrain = self.terrain_map.get_tile((x, y))

            tile = cache.get_image(terrain)
            image_coord = x * tw, y * th
            tile.set_coord(image_coord)

            tile.draw(thumbnail)

            self.shade_tile(thumbnail, terrain, (x, y))

        return thumbnail

    def initialize_shade(self, w, h):
        self.shade = pygame.Surface((w, h)).convert()
        self.shade.fill(SHADE)

    def draw(self, surface):
        if self.view is None:
            surface.blit(self.base_map_surface, (0, 0))
        else:
            vx, vy = self.view.coord
            self.view_rect.topleft = vx * TILEW, vy * TILEH
            surface.blit(self.compiled_image, (0, 0), self.view_rect)

    def draw_thumbnail(self, surface):
        surface.blit(self.thumbnail, (0, 0))

    def shade_tile(self, surface, terrain, (x, y)):

        sw = self.shade.get_width()
        sh = self.shade.get_height()

        if terrain == WATER:
            pass
        elif terrain in (RIVER, DESERT):
            a = self.height_map.get_height((x, y))
            s = MapImage.LOWER_SHADE_LEVEL
            a = -1 * int((a / 100.0) * s) + s
            self.shade.set_alpha(a)
            surface.blit(self.shade, (x * sw, y * sh))
        else:
            a = self.height_map.get_height((x, y))
            s = MapImage.SHADE_LEVEL
            a = -1 * int((a / 100.0) * s) + s
            self.shade.set_alpha(a)
            surface.blit(self.shade, (x * sw, y * sh))

    def render_base_map(self):

        self.initialize_shade(TILEW, TILEH)
        cache = ImageCache.get_instance()

        for x, y in self.terrain_map.all_points:

            terrain = self.terrain_map.get_tile((x, y))

            tile = cache.get_image(terrain)
            image_coord = x * TILEW, y * TILEH
            tile.set_coord(image_coord)

            tile.draw(self.base_map_surface)

            self.shade_tile(self.base_map_surface, terrain, (x, y))

    def compile_map(self):

        self.compiled_image.blit(self.base_map_surface, (0, 0))
        self.compiled_image.blit(self.state.color_overlay.surface, (0, 0))

    def update_image(self):

        self.compile_map()


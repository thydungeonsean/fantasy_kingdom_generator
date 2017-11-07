import pygame
from src.constants import *
import tile_key


class Image(object):
    
    def __init__(self, key, transparent=False):

        self.surface = self.initialize_surface(key, transparent)
        self.coord = (0, 0)
        self.color = None

    def get_tile(self, key):
        return tile_key.tiles[key]

    def get_tile_rect(self):
        return tile_key.tile_rect

    def get_tile_sheet(self):
        return tile_key.load_tile_sheet()

    def get_tile_dim(self):
        return TILEW, TILEH

    def get_base_tile_dim(self):
        return BASE_TILE_W, BASE_TILE_H

    def initialize_surface(self, key, transparent):

        base_w, base_h = self.get_base_tile_dim()

        surface = pygame.Surface((base_w, base_h)).convert()
        surface.fill(BLACK)

        x_offset, y_offset = self.get_tile(key)
        tr = self.get_tile_rect()
        tr.topleft = x_offset*base_w, y_offset*base_h
        surface.blit(self.get_tile_sheet(), (0, 0), tr)

        surface = pygame.transform.scale(surface, self.get_tile_dim()).convert()

        if transparent:
            surface.set_colorkey(COLORKEY)

        return surface
        
    def set_coord(self, coord):
        self.coord = coord
        
    def draw(self, surface):
        surface.blit(self.surface, self.coord)
        
    def run(self):
        pass

    def recolor_image(self, color):

        pix_array = pygame.PixelArray(self.surface)
        pix_array.replace(self.color, color)

        self.color = color

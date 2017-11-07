import src.libtcod.libtcodpy as libtcod
from _map import _Map
from random import randint
import pygame
import math


class HeightMap(_Map):

    DIM = 2
    OCT = 16

    MAX_HEIGHT = 100
    CONTINENT_RADIUS = 40

    def __init__(self, w, h, seed=None):

        _Map.__init__(self, w, h)

        if seed is None:
            self.seed = self.get_new_seed()
        else:
            self.seed = seed

        self.random_gen = libtcod.random_new_from_seed(self.seed)
        self.noise = libtcod.noise_new(HeightMap.DIM, random=self.random_gen)

        self.height_map = self.generate_height_map()
        self.sink_edges()
        self.set_water_level(30)

    @staticmethod
    def get_new_seed():
        return randint(0, 1000000)

    def generate_height_map(self):

        height_map = [[0 for y in range(self.h)] for x in range(self.w)]

        for x, y in self.all_points:

            height = int(self.get_noise_value((x, y)) * HeightMap.MAX_HEIGHT)
            height_map[x][y] = height

        return height_map

    def get_noise_value(self, (x, y)):
        n = libtcod.noise_get_fbm(
            self.noise,
            (x * .05, y * .05),
            HeightMap.OCT
            )
        n = n * .5 + .5  # make range 0 - 1
        return n

    def draw(self, surface):

        i = pygame.Surface((5, 5)).convert()

        for x, y in self.all_points:
            c = int((self.height_map[x][y] / 100.0) * 255)
            # if c < 90:
            #     c = 0
            i.fill((c, c, c))
            surface.blit(i, (x*5, y*5))

    def sink_edges(self):

        for x, y in self.all_points:

            d = math.hypot(x-self.w/2, y-self.h/2)
            if d > HeightMap.CONTINENT_RADIUS:
                diff = int(d - HeightMap.CONTINENT_RADIUS)
                self.height_map[x][y] -= diff * 5
                self.height_map[x][y] = max(0, self.height_map[x][y])

    def set_water_level(self, water):

        above_water_range = float(HeightMap.MAX_HEIGHT - water)

        for x, y in self.all_points:
            if self.height_map[x][y] < water:
                self.height_map[x][y] = 0
            else:
                self.height_map[x][y] = max((self.height_map[x][y] - water, 1))
                ratio = self.height_map[x][y] / above_water_range
                self.height_map[x][y] = int(HeightMap.MAX_HEIGHT * ratio)

    def print_max(self):

        m = 0
        for x, y in self.all_points:
            if self.height_map[x][y] > m:
                m = self.height_map[x][y]
        print m

    def get_height(self, (x, y)):
        return self.height_map[x][y]

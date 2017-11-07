from src.nation.nation import Nation
from src.nation.buildings.capitol import Capitol
from src.nation.terrain_affinity import TerrainAffinity
from random import randint, sample
from src.constants import *
from src.nation.peoples.peoples import PEOPLES
from src.nation.peoples.people import People
from src.nation.population import Population


class NationGenerator(object):

    START_ZONE_RANGE = 10

    terrain_code_to_str = TerrainAffinity.code_to_str

    ONE_PEOPLE = 100
    TWO_PEOPLES = 25
    THREE_PEOPLES = 5

    @classmethod
    def generate_nation(cls, state, point, colors):

        # get a terrain_breakdown of starting position

        nation = Nation(state)

        color = colors.pop()
        nation.set_color(color)

        affinity = cls.generate_nation_terrain_affinity(state.terrain_map, point)
        nation.set_terrain_affinity(affinity)

        capitol = Capitol(nation, point)
        nation.add_building(capitol)

        cls.generate_population(nation)

        return nation

    @classmethod
    def generate_nation_terrain_affinity(cls, terrain_map, (px, py)):

        terrain_count = cls.get_terrain_count(terrain_map, (px, py))

        kwargs = cls.create_terrain_kwargs(terrain_count)

        return TerrainAffinity(**kwargs)

    @classmethod
    def get_terrain_count(cls, terrain_map, (px, py)):
        r = cls.START_ZONE_RANGE
        points_in_zone = [(x, y) for x in range(px - r, px + r) for y in range(py - r, py + r)
                          if terrain_map.point_in_bounds((x, y))]
        terrain_count = {}
        for point in points_in_zone:
            terrain = terrain_map.get_tile(point)
            if terrain == WATER:
                continue
            if terrain_count.get(terrain, None) is None:
                terrain_count[terrain] = 1
            else:
                terrain_count[terrain] += 1
        terrain_count[terrain_map.get_tile((px, py))] += 1  # weight the capitol extra
        return terrain_count

    @classmethod
    def create_terrain_kwargs(cls, terrain_count):

        keys = sorted(terrain_count.keys(), key=lambda x: terrain_count[x], reverse=True)

        roll = randint(0, min(2, len(keys)-1))
        if roll == 0:
            kwargs = cls.choose_keys(keys, 1, (5,))
        elif roll == 1:
            kwargs = cls.choose_keys(keys, 2, (4, 3))
        else:  # roll == 2
            kwargs = cls.choose_keys(keys, 3, (3, 2, 2))

        return kwargs

    @classmethod
    def choose_keys(cls, keys, num, values):
        kwargs = {}
        for i in range(num):
            kwargs[cls.terrain_code_to_str[keys[i]]] = values[i]
        return kwargs

    @classmethod
    def generate_population(cls, nation):

        population = nation.population

        roll = randint(0, 99)

        num = 1

        if roll < cls.THREE_PEOPLES:
            num = 3
        elif roll < cls.TWO_PEOPLES:
            num = 2

        people_keys = sample(PEOPLES, num)
        for p in people_keys:
            people = People(p, nation)
            population.add_people(people)

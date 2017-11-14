from random import *
from src.constants import *


class RiverGenerator(object):

    NUM_RIVERS = 10
    RIVER_SPACING = 10
    RIVER_SIZE = 10

    @classmethod
    def generate_rivers(cls, terrain):

        short_dist_map = cls.generate_shore_distance_map(terrain)

        river_count = 0

        valid_river_sources = cls.find_valid_river_sources(terrain)

        river_points = set()

        while valid_river_sources and river_count <= cls.NUM_RIVERS:
            new_river_source = choice(valid_river_sources)
            river_destination = cls.generate_river_destination(terrain, new_river_source)
            terrain.set_tile(new_river_source, RIVER)

            river_points.update(cls.generate_new_river(terrain, short_dist_map, new_river_source, river_destination))
            river_count += 1

            valid_river_sources = cls.find_valid_river_sources(terrain)

        for point in river_points:
            terrain.set_tile(point, RIVER)

    @classmethod
    def find_valid_river_sources(cls, terrain):
        mountains = set(terrain.get_all(MOUNTAIN))
        rivers = terrain.get_all(RIVER)
        too_near_river = cls.find_zone_too_near_river(rivers, terrain)
        return list(mountains.difference(too_near_river))

    @classmethod
    def find_zone_too_near_river(cls, rivers, terrain):
        too_near = set()
        for rx, ry in rivers:
            for x in range(rx - cls.RIVER_SPACING, rx + cls.RIVER_SPACING):
                for y in range(ry - cls.RIVER_SPACING, ry + cls.RIVER_SPACING):
                    if terrain.point_in_bounds((x, y)):
                        too_near.add((x, y))

        return too_near

    @classmethod
    def generate_new_river(cls, terrain, short_dist_map, source, dest):

        dest_map = cls.get_dijkstra(dest, terrain)
        river_points = [source]

        shore = set(filter(lambda x: terrain.adj_to_water(x), terrain.all_points))

        while True:
            river_edge = river_points[-1]
            next_point = cls.get_next_river_point(river_points, river_edge, terrain, short_dist_map,
                                                  dest_map)

            if not next_point:
                break
            elif terrain.get_tile(next_point) == WATER:
                river_points.append(next_point)
                break
            else:
                river_points.append(next_point)

            if next_point in shore:
                break

        # return a set of points to be set into river tiles
        return set(river_points)

    @classmethod
    def get_next_river_point(cls, river, (x, y), terrain, short_dist_map, dest_map):

        possible = filter(lambda r: r not in river, terrain.get_adj((x, y)))
        possible = filter(lambda r: cls.not_adj_to_river(terrain, r, river), possible)

        weights = {}
        for point in possible:
            shore_value = int(short_dist_map.get(point, 0) ** .9 * randint(4, 9) * .1)
            #dest_value = int(dest_map.get(point, 20)**1.5)
            weights[point] = terrain.height_map.get_height((x, y)) + shore_value #+ dest_value

        ordered = sorted(weights.keys(), key=lambda x: weights[x])
        if ordered:
            best = ordered[0]

            if weights[best] > terrain.height_map.get_height((x, y)) + short_dist_map.get((x, y), 0): # + \
                #dest_map.get((x, y), 20)**1.5:
                return False

            return best
        else:
            return False

    @classmethod
    def not_adj_to_river(cls, terrain, (x, y), river):

        adj = set(terrain.get_adj((x, y)))
        blocking_river = river[:]
        blocking_river.pop(-1)
        return not adj.intersection(set(blocking_river))

    @classmethod
    def generate_river_destination(cls, terrain, (rx, ry)):

        def close_to_start((x, y)):
            value = (abs(rx - x) + abs(ry - y))
            return 15 <= value <= 30

        shore = filter(lambda x: terrain.adj_to_water(x), terrain.all_points)
        valid = filter(close_to_start, shore)
        if valid:
            return [choice(valid)]
        else:
            return []

    @classmethod
    def generate_shore_distance_map(cls, terrain):

        shore = filter(lambda x: terrain.adj_to_water(x), terrain.all_points)
        dist_map = cls.get_dijkstra(shore, terrain)

        return dist_map

    @classmethod
    def get_next_edge(cls, terrain, edge):
        next_edge = set()

        for point in edge:
            adj = terrain.get_adj(point)
            for a in adj:
                next_edge.add(a)
        return list(next_edge)

    @classmethod
    def get_dijkstra(cls, edge, terrain, limit=None):

        d_map = {}

        touched = set()
        value = 0

        while edge:
            for point in edge:
                touched.add(point)
                if d_map.get(point) is None:
                    d_map[point] = value
                elif value < d_map.get(point):
                    d_map[point] = value

            next_edge = cls.get_next_edge(terrain, edge)
            edge = list(filter(lambda x: cls.tile_passable(terrain, x) and x not in touched, next_edge))

            value += 1
            if limit is not None and value > limit:
                break

        return d_map

    @classmethod
    def tile_passable(cls, terrain, point):
        return terrain.get_tile(point) != WATER

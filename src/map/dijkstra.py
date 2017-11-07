

def get_next_edge(self, edge):
    next_edge = set()

    for point in edge:
        adj = self.terrain_map.get_adj(point)
        for a in adj:
            next_edge.add(a)
    return list(next_edge)


def get_dijkstra(self, edge, passable, limit=None):
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

        next_edge = self.get_next_edge(edge)
        edge = list(filter(passable and x not in touched, next_edge))

        value += 1
        if limit is not None and value > limit:
            break

    return d_map


def tile_passable(self, point):
    return self.terrain_map.get_tile(point) in PathFindingMap.PASSABLE

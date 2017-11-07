

class _Map(object):

    def __init__(self, w, h):

        self.w = w
        self.h = h

    @property
    def all_points(self):
        for y in range(self.h):
            for x in range(self.w):
                yield (x, y)

    def point_in_bounds(self, (x, y)):
        return 0 <= x < self.w and 0 <= y < self.h

    def get_adj(self, (x, y)):

        adj = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        return filter(self.point_in_bounds, adj)

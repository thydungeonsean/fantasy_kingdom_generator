from src.map_object.army import Army


class Military(object):

    def __init__(self, nation):

        self.nation = nation
        self.state = self.nation.state
        self.armies = []

    def add_army(self, pos, points=10):

        new_army = Army(self.nation, pos, points=points)
        self.armies.append(new_army)

    def draw_armies(self, surface):

        for army in filter(lambda x: self.object_visible(x), self.armies):
            army.draw(surface)

    def object_visible(self, obj):
        return self.state.view.coord_in_view(obj.coord)

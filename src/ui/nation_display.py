from element import Element
from src.constants import *
from font_draw import FontDraw


class NationDisplay(Element):

    w = SCALE * 400
    h = SCALE * 400

    coord = SCALE * 25, SCALE * 25

    cell_w = SCALE * 200
    cell_h = SCALE * 25

    def __init__(self, nation):

        Element.__init__(self, NationDisplay.coord, NationDisplay.w, NationDisplay.h)

        self.nation = nation
        self.color = nation.color

        self.nation.stats.compute()  # make sure they're up to date
        self.render_display()
        self.surface.set_alpha(150)

    def render_display(self):

        row = 0
        self.draw_text(0, row, self.nation.name)

        for terrain in self.nation.stats.favoured_terrain:
            self.draw_text(0, row, ''.join(('Favoured Terrain: ', terrain)))
            row += 1

        self.draw_text(0, 9, 'Troops:')
        row = 10
        for u in self.nation.population.troop_list:
            unit_name = ' '.join(map(str.capitalize, u.split('_')))
            self.draw_text(0, row, unit_name)
            row += 1


    def draw_text(self, col, row, text):

        text_image = FontDraw.get_instance().create_text_box(text, self.color,
                                                             NationDisplay.cell_w, NationDisplay.cell_h)
        self.surface.blit(text_image, (NationDisplay.cell_w * col, NationDisplay.cell_h * row))

    def draw_text_wide(self, row, text):
        text_image = FontDraw.get_instance().create_text_box(text, self.color,
                                                             NationDisplay.cell_w* 3, NationDisplay.cell_h)
        self.surface.blit(text_image, (0, NationDisplay.cell_h * row))
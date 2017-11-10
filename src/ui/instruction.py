from element import Element
from src.constants import *
from font_draw import FontDraw


class Instruction(Element):

    w = SCALE * 600
    h = SCALE * 50

    coord = (SCREENW - w) / 2, SCALE * 50

    color = WHITE

    def __init__(self, text):

        Element.__init__(self, Instruction.coord, Instruction.w, Instruction.h)

        self.render_text(text)
        self.surface.set_colorkey(BLACK)
        self.alpha = 0
        self.fade_mod = 15

    def run(self):

        self.alpha += self.fade_mod
        if self.alpha > 255:
            self.fade_mod *= -1
            self.alpha = 255
        elif self.alpha <= 0:
            self.fade_mod *= -1
            self.alpha = 0

        self.surface.set_alpha(self.alpha)

    def render_text(self, text):
        text_image = FontDraw.get_instance().create_text_box(text, Instruction.color, self.w, self.h)
        self.surface.blit(text_image, (0, 0))

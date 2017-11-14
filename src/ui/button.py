from src.constants import *
from border import Border
from font_draw import FontDraw
from element import Element


class Button(Element):

    BUTTON_W = SCALE * 200
    BUTTON_H = SCALE * 40

    START_COLOR = WHITE
    HIGHLIGHT_COLOR = YELLOW

    def __init__(self, coord, text):

        w, h = self.get_panel_dim()
        Element.__init__(self, coord, w, h)

        self.color = Button.START_COLOR

        self.border = Border(self, self.color)
        self.text = text

        self.render_image()

    def get_panel_dim(self):
        return Button.BUTTON_W, Button.BUTTON_H

    def click(self, point):
        if self.point_is_over(point):
            self.on_click()
            return True
        return False

    def on_click(self):
        pass
        print self.text

    def render_image(self):
        text_image = FontDraw.get_instance().create_text_box(self.text, self.color, self.w, self.h)
        self.surface.blit(text_image, (0, 0))
        self.border.draw(self.surface)

    def update_button(self):
        self.render_image()

    def highlight(self):
        self.color = Button.HIGHLIGHT_COLOR
        self.border.change_color(self.color)
        self.update_button()

    def normal(self):
        self.color = Button.START_COLOR
        self.border.change_color(self.color)
        self.update_button()


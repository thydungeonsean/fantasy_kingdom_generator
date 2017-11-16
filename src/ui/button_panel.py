from src.constants import *
from button import Button
from font_draw import FontDraw


class ButtonPanel(Button):

    PANEL_W = SCALE * 10 + Button.BUTTON_W

    TITLE_W = PANEL_W
    TITLE_H = Button.BUTTON_H

    START_COLOR = WHITE
    HIGHLIGHT_COLOR = YELLOW

    def __init__(self, coord, text, num_buttons=3):

        self.num_buttons = num_buttons
        Button.__init__(self, coord, text)
        self.render_image()

    def get_panel_dim(self):
        return ButtonPanel.PANEL_W, (self.num_buttons + 1) * (Button.BUTTON_H + SCALE*5) + SCALE*5

    def render_image(self):
        cls = ButtonPanel
        text_image = FontDraw.get_instance().create_text_box(self.text, self.color, cls.TITLE_W, cls.TITLE_H)
        self.surface.blit(text_image, (0, 0))
        self.border.draw(self.surface)

    def click(self, point):
        return False

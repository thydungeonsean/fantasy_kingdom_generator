import pygame
from src.constants import *


class MouseHandler(object):

    def __init__(self, state):

        self.state = state

    def left_click(self):

        ui_clicked = self.click_ui()

    def get_mouse_coord(self):
        mx, my = pygame.mouse.get_pos()
        relx = mx / TILEW
        rely = my / TILEH
        relx += self.state.view.coord[0]
        rely += self.state.view.coord[1]
        return relx, rely

    def click_ui(self):

        pos = pygame.mouse.get_pos()
        return self.state.ui.click(pos)
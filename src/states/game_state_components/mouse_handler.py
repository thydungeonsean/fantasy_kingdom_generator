import pygame
from src.constants import *
from src.ui.nation_display import NationDisplay
from src.ui.instruction import Instruction
from src.ui.nation_chooser_button import NationChooserButton


class MouseHandler(object):

    def __init__(self, state):

        self.state = state

    @property
    def ui(self):
        return self.state.ui

    def left_click(self):

        ui_clicked = self.click_ui()
        if not ui_clicked and self.state.power_manager.selected_power is not None:
            self.click_power()

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

    def right_click(self):

        self.clear_panels()
        coord = self.get_mouse_coord()
        nation = self.state.nation_list.get_nation_at_point(coord)
        if nation is not None:
            self.open_nation_panel(nation)

    def open_nation_panel(self, nation):

        self.clear_panels()
        nation_display = NationDisplay(nation)
        self.ui.add_key_element(nation_display, 'open_panel')

        if self.state.mode == self.state.NATION_CHOOSE:
            nation_chooser = NationChooserButton(nation)
            self.ui.add_key_element(nation_chooser, 'nation_chooser')

    def clear_panels(self):

        if self.ui.key_element_dict.get('open_panel', None) is not None:
            self.ui.remove_key_element('open_panel')
            if self.state.mode == self.state.NATION_CHOOSE and \
                    self.ui.key_element_dict.get('nation_chooser', None) is not None:
                self.ui.remove_key_element('nation_chooser')

    def click_power(self):

        self.state.power_manager.selected_power.click(self.get_mouse_coord())

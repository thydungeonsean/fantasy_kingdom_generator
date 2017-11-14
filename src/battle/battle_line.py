from src.constants import *
from src.ui.battle.battle_field_panel import BattleFieldPanel
import pygame


class BattleLine(object):

    # left = 'l' right = 'r'

    w = 2 * UNITW
    h = 7 * UNITH

    w_buffer = SCALE * 75
    h_buffer = SCALE * 75

    coord_dict = {'l': (w_buffer, BattleFieldPanel.panel_h - h - h_buffer),
                  'r': (BattleFieldPanel.panel_w - w - w_buffer, BattleFieldPanel.panel_h - h - h_buffer)}

    CHARGING = 0
    DEFENDING = 1
    ADVANCING = 2

    def __init__(self, state, army, facing, panel):

        self.state = state
        self.army = army
        self.units = None
        self.facing = facing
        self.panel = panel

        self.w = 2 * UNITW
        self.h = 7 * UNITH

        self.background = pygame.Surface((self.w, self.h)).convert()
        self.background.fill(BLACK)
        self.coord = self.get_battleline_coord()

        self.coord_list = [(x, y) for x in range(2) for y in range(7)]
        self.disposition = None

        self.initialize()

    def draw(self, surface):

        surface.blit(self.background, self.coord)

        frame = self.state.frame
        for unit in self.units:
            unit.draw(surface, frame, self.facing)

    def initialize(self):

        self.create_units()
        self.deploy_army()
        self.init_disposition()

    def init_disposition(self):
        self.set_disposition(BattleLine.ADVANCING)

    def set_disposition(self, disp):
        self.disposition = disp

    def get_battleline_coord(self):

        px, py = self.panel.coord
        cx, cy = BattleLine.coord_dict[self.facing]
        return px + cx, py + cy

    def deploy_army(self):
        from random import shuffle

        shuffle(self.units)
        u = 0

        for unit in self.units:
            coord = self.coord_list[u]
            self.position_unit(unit, coord)
            u += 1

        pass

    def position_unit(self, unit, (x, y)):

        bx, by = self.coord

        if self.facing == 'l':
            ux = UNITW - (x*UNITW) + bx
        else:
            ux = x * UNITW + bx


        uy = y * UNITH + by

        unit.set_coord((x, y))
        unit.set_image_coord((ux, uy))


    def create_units(self):
        self.units = self.army.build_army()

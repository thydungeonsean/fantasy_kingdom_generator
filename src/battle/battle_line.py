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

    coord_list = [(x, y) for x in range(2) for y in range(7)]

    def __init__(self, state, army, side, panel):

        self.state = state
        self.army = army
        self.units = None
        self.side = side
        self.panel = panel

        self.w = 2 * UNITW
        self.h = 7 * UNITH

        self.background = pygame.Surface((self.w, self.h)).convert()
        self.background.fill(BLACK)
        self.coord = self.get_battleline_coord()

        self.coord_list = BattleLine.coord_list
        self.disposition = None

        self.pierced = 0

        self.initialize()

    @property
    def frame(self):
        return self.state.frame

    def draw_unit(self, unit, surface):
        unit.draw(surface, self.frame, self.side)

    def draw_unit_effect(self, unit_image, surface):
        image_key = '_'.join((self.side, self.frame))
        unit_image.draw_animated(surface, unit_image.image_coord, image_key)

    def draw(self, surface):

        surface.blit(self.background, self.coord)

        for unit in self.units:
            self.draw_unit(unit, surface)

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
        cx, cy = BattleLine.coord_dict[self.side]
        return px + cx, py + cy

    def deploy_army(self):
        from random import shuffle

        shuffle(self.units)
        coords = self.coord_list[:]
        shuffle(coords)
        u = 0

        for unit in self.units:
            coord = coords[u]
            self.position_unit(unit, coord)
            u += 1

    def get_image_coord(self, (x, y)):
        bx, by = self.coord
        if self.side == 'l':
            ux = UNITW - (x*UNITW) + bx
        else:
            ux = x * UNITW + bx

        uy = y * UNITH + by
        return ux, uy

    def position_unit(self, unit, (x, y)):

        unit.set_coord((x, y))
        unit.set_image_coord(self.get_image_coord((x, y)))

    def create_units(self):
        self.units = self.army.build_army()

    def point_is_over(self, (x, y)):
        sx, sy = self.coord
        return sx <= x < sx + self.w and sy <= y < sy + self.h

    def remove_unit(self, unit):
        self.units.remove(unit)
        self.state.effect_manager.fade_unit(unit, self)

    def rout_unit(self, unit):
        # flag to be destroyed
        # update battle scale accordingly
        self.remove_unit(unit)

    def get_unit_at_coord(self, coord):
        at_coord = filter(lambda u: u.coord == coord, self.units)
        if len(at_coord) == 0:
            return None
        else:
            return at_coord[0]

    def take_hits(self, hits, row):

        front_unit = self.get_unit_at_coord((0, row))
        back_unit = self.get_unit_at_coord((1, row))
        if front_unit is not None:
            unit = front_unit
        elif back_unit is not None:
            unit = back_unit
        else:
            unit = None

        if unit is None:
            self.take_piercing_hits(hits)
        else:
            unit.take_hits(hits)
            self.state.effect_manager.flash_unit(unit, self, hits)
            if unit.dead:
                self.rout_unit(unit)

    def take_piercing_hits(self, hits):
        self.pierced += hits
        print 'the battle line took %d piercing hits' % hits



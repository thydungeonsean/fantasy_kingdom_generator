import pygame
from src.constants import *
from random import choice


class BattleHighlighter(object):

    SQUARE = 0
    FULL = 1
    SELECTED = 2
    main_colors = (WHITE, YELLOW, YELLOW)
    select_colors = (WHITE, CYAN, MED_CYAN)

    def __init__(self, state):

        cls = BattleHighlighter

        self.state = state
        self.color_code = self.choose_color_code()

        self.select_color = cls.select_colors
        self.main_color = cls.main_colors

        self.highlights = []
        self.draw_highlight = {
            cls.SQUARE: self.draw_square_highlight,
            cls.FULL: self.draw_full_highlight,
            cls.SELECTED: self.draw_selected_highlight,
        }
        self.square_rect = pygame.Rect((0, 0), (UNITW-1, UNITH-1))
        self.full_rect = pygame.Rect((0, 0), (UNITW*2-1, UNITH*7-1))

        self.tick = 0

    def add_square(self, point):
        self.highlights.append((BattleHighlighter.SQUARE, point))

    def add_selected_square(self, point):
        self.highlights.append((BattleHighlighter.SELECTED, point))

    def add_full(self, point):
        self.highlights.append((BattleHighlighter.FULL, point))

    def clear(self):
        del self.highlights[:]

    def run(self):
        if len(self.highlights) > 0:
            self.tick += 1
            if self.tick >= 3:
                self.tick = 0
                self.color_code = self.choose_color_code()

    @staticmethod
    def choose_color_code():
        return choice((0, 1, 2))

    def draw(self, surface):

        for key, point in self.highlights:
            self.draw_highlight[key](point, surface)

    def draw_square_highlight(self, point, surface):

        self.square_rect.topleft = point
        pygame.draw.rect(surface, self.main_color[self.color_code], self.square_rect, SCALE)

    def draw_selected_highlight(self, point, surface):
        self.square_rect.topleft = point
        pygame.draw.rect(surface, self.select_color[self.color_code], self.square_rect, SCALE)

    def draw_full_highlight(self, point, surface):

        self.full_rect.topleft = point
        pygame.draw.rect(surface, self.main_color[self.color_code], self.full_rect, SCALE)

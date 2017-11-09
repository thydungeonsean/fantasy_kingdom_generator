import pygame
from src.constants import *
from src.ui.font_draw import FontDraw


class ProgressBar(object):

    bar_w = SCREENW - SCREENW / 3
    bar_h = SCALE * 25
    bar_x = (SCREENW - bar_w) / 2
    bar_y = (SCREENH - bar_h) / 2

    load_bar = pygame.Surface((bar_w, bar_h))

    COLOR = WHITE
    text_w = bar_w
    text_h = 25*SCALE
    text_coord = ((bar_x-0), (bar_y - text_h))

    @classmethod
    def draw_load_bar(cls, message, progress):

        screen = pygame.display.get_surface()
        cls.clear_screen()

        cls.draw_message(message)

        bar = cls.load_bar.convert(screen)
        bar.fill(UNFILLED_BAR)

        prog_w = int(cls.bar_w * progress)
        progress_rect = pygame.Rect((0, 0), (prog_w, cls.bar_h))

        pygame.draw.rect(bar, PROGRESS_BAR, progress_rect, 0)

        screen.blit(bar, (cls.bar_x, cls.bar_y))

        pygame.display.update()

    @classmethod
    def clear_screen(cls, update=False):
        screen = pygame.display.get_surface()
        screen.fill(BLACK)
        if update:
            pygame.display.update()

    @classmethod
    def draw_message(cls, message):

        f = FontDraw.get_instance()

        box = f.create_text_box(message, cls.COLOR, cls.text_w, cls.text_h)

        screen = pygame.display.get_surface()
        screen.blit(box, cls.text_coord)

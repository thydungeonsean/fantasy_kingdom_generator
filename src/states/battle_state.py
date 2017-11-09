from abstract_state import AbstractState
from src.ui.ui import UI
import pygame
from pygame.locals import *


class BattleState(AbstractState):

    def __init__(self, state_manager, attacker, defender):

        AbstractState.__init__(self, state_manager)

        self.initialize()

    def initialize(self):
        pass

    def initialize_ui(self):
        return UI.create_battle_mode_ui(self)

    def handle_input(self):

        # returns true to exit game
        for event in pygame.event.get():

            if event.type == QUIT:
                self.trigger_exit()

            elif event.type == KEYDOWN:

                if event.key == K_ESCAPE:
                    pass

            elif event.type == KEYUP:

                pass

            elif event.type == MOUSEBUTTONDOWN:

                if event.button == 1:
                    self.ui.click(pygame.mouse.get_pos())

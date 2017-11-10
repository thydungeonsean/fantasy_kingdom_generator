from abstract_state import AbstractState
from src.ui.ui import UI
import pygame
from src.constants import *


class InGameMenuState(AbstractState):

    def __init__(self, state_manager, game_state):

        AbstractState.__init__(self, state_manager)
        self.game_state = game_state
        self.back_drop = self.get_screen_image()

        self.run = self.first_run

    def init_screen(self):

        self.screen.fill(BLACK)
        self.screen.blit(self.back_drop, (0, 0))

    def get_screen_image(self):

        back_drop = self.game_state.screen

        surf = pygame.Surface((SCREENW, SCREENH)).convert()
        surf.blit(back_drop, (0, 0))
        surf.set_alpha(100)
        return surf

    def handle_input(self):

        # returns true to exit game
        for event in pygame.event.get():

            if event.type == QUIT:
                self.trigger_exit()

            elif event.type == KEYDOWN:

                if event.key == K_ESCAPE:
                    self.return_to_game()

            elif event.type == KEYUP:

                pass

            elif event.type == MOUSEBUTTONDOWN:

                if event.button == 1:
                    self.ui.click(pygame.mouse.get_pos())

    def initialize_ui(self):
        return UI.create_in_game_menu_ui(self)

    def draw(self):

        self.ui.draw(self.screen)

    def generate_new_world(self):
        game = self.state_manager.load_new_game()
        self.set_next_state(game)
        self.trigger_exit()

    def return_to_main_menu(self):
        main_menu = self.state_manager.load_main_menu()
        self.set_next_state(main_menu)
        self.trigger_exit()

    def return_to_game(self):
        self.set_next_state(self.game_state)
        self.game_state.reset_state()
        self.trigger_exit()

    def quit_program(self):
        self.set_next_state('exit')
        self.trigger_exit()

    def first_run(self):
        self.init_screen()
        self.run = self.base_run

    def base_run(self):
        pass

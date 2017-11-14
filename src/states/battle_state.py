from abstract_state import AbstractState
from src.ui.ui import UI
import pygame
from pygame.locals import *
from src.constants import *
from src.ui.battle.battle_field_panel import BattleFieldPanel
from src.battle.battle_line import BattleLine
from battle_state_components.turn_structure import TurnStructure
from src.ui.battle.disposition_chooser import DispositionChooser


class BattleState(AbstractState):

    A = 'a'
    B = 'b'

    ANI_RATE = 20

    def __init__(self, state_manager, game, attacker, defender):

        self.game_state = game
        self.attacker = attacker
        self.defender = defender
        self.player_controlled, self.ai_controlled = self.set_player_controlled()
        self.sides = {self.attacker: 'l', self.defender: 'r'}

        AbstractState.__init__(self, state_manager)
        self.subscreen = self.set_subscreen()
        self.back_drop = self.get_screen_image()
        self.panel = BattleFieldPanel(self)
        self.battle_lines = {'l': BattleLine(self, attacker, 'l', self.panel),
                             'r': BattleLine(self, defender, 'r', self.panel)}
        self.turn_structure = TurnStructure(self)

        self.frame = BattleState.A
        self.frame_tick = 0

        self.run = self.first_run
        self.initialize()

    def init_screen(self):

        self.subscreen.blit(self.back_drop, (0, 0))
        self.panel.draw(self.subscreen)
        self.screen.blit(self.subscreen, (0, 0))

    def first_run(self):
        self.init_screen()
        self.run = self.state_run

    def reset_state(self):
        self.run = self.first_run
        self.set_next_state('exit')
        self.exit_state = False

    def set_player_controlled(self):
        if self.game_state.player_nation == self.attacker.nation:
            return self.attacker, self.defender
        elif self.game_state.player_nation == self.defender.nation:
            return self.defender, self.attacker
        else:
            print 'no controller, pick random for testing'
            from random import shuffle
            armies = [self.attacker, self.defender]
            shuffle(armies)
            return armies

    def get_battle_line_by_key(self, key):
        if key in ('l', 'r'):
            return self.battle_lines[key]
        else:
            side = self.sides[key]
            print side
            return self.battle_lines[side]

    def get_screen_image(self):

        surf = pygame.Surface((SCREENW, SCREENH)).convert()
        surf.blit(self.game_state.subscreen, (0, 0))
        surf.set_alpha(100)

        back_drop = pygame.Surface((SCREENW, SCREENH)).convert()
        back_drop.fill(BLACK)
        back_drop.blit(surf, (0, 0))

        return back_drop

    def initialize(self):
        self.panel.update()
        self.turn_structure.start_new_turn()

    def initialize_ui(self):
        return UI.create_battle_mode_ui(self)

    def handle_input(self):

        # returns true to exit game
        for event in pygame.event.get():

            if event.type == QUIT:
                self.trigger_exit()

            elif event.type == KEYDOWN:

                if event.key == K_ESCAPE:
                    self.open_in_game_menu()
                elif event.key == K_l:
                    self.open_disp_choose()

            elif event.type == KEYUP:

                pass

            elif event.type == MOUSEBUTTONDOWN:

                if event.button == 1:
                    self.ui.click(pygame.mouse.get_pos())

    def draw(self):

        self.panel.draw(self.subscreen)

        for bl in self.battle_lines.values():
            bl.draw(self.subscreen)

        self.screen.blit(self.subscreen, (0, 0))
        self.ui.draw(self.screen)

    def state_run(self): # real run function

        self.tick()

    def tick(self):

        self.frame_tick += 1
        if self.frame_tick >= BattleState.ANI_RATE:
            self.switch_frame()
            self.frame_tick = 0

    def switch_frame(self):

        if self.frame == BattleState.A:
            self.frame = BattleState.B
        else:
            self.frame = BattleState.A

    # state change functions
    def open_in_game_menu(self):

        state = self.state_manager.load_in_game_menu(self)
        self.set_next_state(state)
        self.trigger_exit()

    def open_disp_choose(self):
        DispositionChooser(self, self.ui, self.sides[self.player_controlled]).add_to_state()


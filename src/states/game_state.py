from abstract_state import *
from game_state_components.view import View
from src.map.map_image import MapImage
from src.map.procgen.map_generator import MapGenerator
from src.ui.ui import UI
from src.map.influence_map import InfluenceMap
from src.map.color_overlay import ColorOverlay
from game_state_components.nation_list import NationList
from src.map.procgen.nation_gen.nation_placer import NationPlacer
from game_state_components.mouse_handler import MouseHandler
from game_state_components.cursor import Cursor


class GameState(AbstractState):

    # mode keys
    NATION_CHOOSE = 0
    STRATEGIC = 1
    BATTLE = 2

    def __init__(self, state_manager):

        AbstractState.__init__(self, state_manager)

        self.nation_list = NationList(self)

        # map
        self.height_map = MapGenerator.generate_height_map()
        self.terrain_map = MapGenerator.generate_terrain_map(self.height_map)

        self.influence_map = InfluenceMap(self.terrain_map, self)
        self.color_overlay = ColorOverlay(self.influence_map)

        self.map_image = MapImage(self.terrain_map, self.height_map, state=self)

        # nations
        NationPlacer.generate_nations(self)

        # game_state_components
        self.view = View(self)
        self.subscreen = self.set_subscreen()
        self.mouse_handler = MouseHandler(self)
        self.cursor = Cursor(self)

        # fields
        self.mode = GameState.NATION_CHOOSE
        self.player_nation = None

        self.initialize()

    def initialize(self):

        self.map_image.set_view(self.view)
        self.color_overlay.set_view(self.view)
        self.map_image.compile_map()

    def initialize_ui(self):

        return UI.create_nation_choose_ui(self)

    def switch_ui(self, mode):
        if mode == 'strategic':
            new_ui = UI.create_strategic_mode_ui(self)
        elif mode == 'battle':
            new_ui = UI.create_battle_mode_ui(self)
        else:
            raise Exception('invalid ui key')
        self.ui = new_ui

    def handle_input(self):

        # returns true to exit game
        for event in pygame.event.get():

            if event.type == QUIT:
                self.game_over()

            elif event.type == KEYDOWN:

                if event.key == K_ESCAPE:
                    self.open_in_game_menu()

                elif event.key == UP:
                    self.view.press('up')
                elif event.key == DOWN:
                    self.view.press('down')
                elif event.key == RIGHT:
                    self.view.press('right')
                elif event.key == LEFT:
                    self.view.press('left')

                elif event.key == K_SPACE:
                    # self.advance_turn()
                    self.trigger_mock_battle()

            elif event.type == KEYUP:
                if event.key == UP:
                    self.view.release('up')
                elif event.key == DOWN:
                    self.view.release('down')
                elif event.key == RIGHT:
                    self.view.release('right')
                elif event.key == LEFT:
                    self.view.release('left')

            elif event.type == MOUSEBUTTONDOWN:

                if event.button == 1:
                    self.mouse_handler.left_click()
                    self.place_settlement(self.mouse_handler.get_mouse_coord())

                elif event.button == 3:  # right click
                    self.mouse_handler.right_click()

            elif event.type == MOUSEMOTION:

                self.cursor.update()

    def trigger_exit(self):
        self.exit_state = True

    def run(self):

        self.ui.run()
        self.view.run()

    def draw(self):

        self.map_image.draw(self.subscreen)
        # self.map_image.draw_thumbnail(self.screen)

        self.nation_list.draw(self.subscreen)

        self.cursor.draw(self.subscreen)

        self.screen.blit(self.subscreen, (0, 0))
        self.ui.draw(self.screen)

    def game_over(self):

        self.set_next_state('exit')
        self.trigger_exit()

    def advance_turn(self):

        self.nation_list.grow_nations()
        self.map_image.update_image()

    def place_settlement(self, point):

        nation = self.nation_list.get_nation_at_point(point)
        if nation is not None:
            nation.add_settlement(point)

    def choose_nation(self, nation):

        self.ui.remove_key_element('nation_chooser')

        self.mode = GameState.STRATEGIC
        self.player_nation = nation
        self.switch_ui('strategic')

    # state change functions
    def open_in_game_menu(self):

        state = self.state_manager.load_in_game_menu(self)
        self.set_next_state(state)
        self.trigger_exit()

    def trigger_mock_battle(self):

        from random import sample, choice
        from src.map_object.army import Army
        nations = sample(self.nation_list.nation_list, 2)

        if self.player_nation is not None:
            attacker = Army(self.player_nation, (0, 0))
        else:
            attacker = Army(nations[0], (0, 0))
        point = choice(self.terrain_map.get_all(DESERT))

        defender = Army(nations[1], point)

        state = self.state_manager.start_battle(self, attacker, defender)
        self.set_next_state(state)
        self.trigger_exit()

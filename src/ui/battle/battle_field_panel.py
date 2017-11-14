import pygame
from ..font_draw import FontDraw
from battle_layout import *


class BattleFieldPanel(object):

    panel_w = battle_field['panel_w']
    panel_h = battle_field['panel_h']
    coord = battle_field['coord']

    cell_w = SCALE * 200
    cell_h = SCALE * 25

    color = WHITE

    CHARGING = 0
    DEFENDING = 1
    ADVANCING = 2

    disposition_key = {
        CHARGING: 'Charging',
        DEFENDING: 'Defending',
        ADVANCING: 'Advancing'
    }

    terrain_key = {
        LOWLAND: 'Lowlands',
        FOREST: 'Forest',
        HIGHLAND: 'Highlands',
        RIVER: 'Riverlands',
        SWAMP: 'Swamps',
        ROUGH: 'Wilderness',
        MOUNTAIN: 'Mountains',
        DESERT: 'Desert',
    }

    def __init__(self, state):

        self.state = state

        self.image = self.init_image()

    def draw(self, surface):

        surface.blit(self.image, BattleFieldPanel.coord)

    def init_image(self):

        image = pygame.Surface((BattleFieldPanel.panel_w, BattleFieldPanel.panel_h)).convert()

        return image

    def update(self):
        self.render_panel()

    def render_panel(self):

        self.image.fill(BLACK)

        attacker_color = self.state.attacker.color
        defender_color = self.state.defender.color

        self.draw_text(0, 0, self.get_battle_title(), wide=True)
        self.draw_text(0, 1, ' '.join(('Terrain:', self.get_battle_terrain())))

        self.draw_text(0, 4, 'Attackers', color=attacker_color)
        self.draw_text(2, 4, 'Defenders', color=defender_color)

        self.draw_text(0, 6, self.get_disposition('l'), color=attacker_color)
        self.draw_text(2, 6, self.get_disposition('r'), color=defender_color)

        player_col = self.find_player_col()
        self.draw_text(player_col, 22, 'Player')

    def draw_text(self, col, row, text, wide=False, color=None):
        cls = BattleFieldPanel
        w = cls.cell_w
        if wide:
            w = cls.panel_w
        if color is None:
            text_color = cls.color
        else:
            text_color = color
        text_image = FontDraw.get_instance().create_text_box(text, text_color, w, cls.cell_h)
        self.image.blit(text_image, (cls.cell_w * col, cls.cell_h * row))

    def get_battle_title(self):
        return ' '.join((self.get_battle_type(), 'in', self.get_name_of_location()))

    def get_battle_type(self):
        # if battle is on a settlement capitol or fortress, call it a siege
        return 'Battle'

    def get_name_of_location(self):
        point = self.state.defender.coord
        game = self.state.game_state
        nation = game.nation_list.get_nation_at_point(point)
        if nation is None:
            name = 'the wilds'
        else:
            name = nation.name
        return name

    def get_battle_terrain(self):
        point = self.state.defender.coord
        terrain = self.state.game_state.terrain_map.get_tile(point)
        return BattleFieldPanel.terrain_key[terrain]

    def get_disposition(self, key):
        disp = BattleFieldPanel.disposition_key[self.state.battle_lines[key].disposition]
        return disp

    def find_player_col(self):
        if self.state.player_controlled == self.state.attacker:
            return 0
        else:
            return 2

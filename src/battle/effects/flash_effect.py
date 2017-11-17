from effect import Effect
from src.image.effect_unit_image import EffectUnitImage
from random import randint


class FlashEffect(Effect):

    def __init__(self, manager, unit, hits, battle_line):

        Effect.__init__(self, manager)

        self.tick = 0
        self.end = 30

        self.hits = hits

        self.battle_line = battle_line
        self.unit = unit
        self.image = EffectUnitImage(self.unit, mode='flash')

    def draw(self, surface):
        if randint(0, 15) <= self.hits:
            self.battle_line.draw_unit_effect(self.image, surface)

    def run(self):
        self.tick += 1
        if self.tick >= self.end:
            self.end_effect()


from effect import Effect
from src.image.effect_unit_image import EffectUnitImage


class FadeEffect(Effect):

    def __init__(self, manager, unit, battle_line):

        Effect.__init__(self, manager)

        self.unit = unit
        self.battle_line = battle_line

        self.image = EffectUnitImage(self.unit, mode='fade')

    def run(self):
        self.image.fade(5)
        if self.image.alpha < 0:
            self.end_effect()

    def draw(self, surface):
        self.battle_line.draw_unit_effect(self.image, surface)


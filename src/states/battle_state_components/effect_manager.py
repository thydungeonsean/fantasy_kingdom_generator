from src.battle.effects.flash_effect import FlashEffect
from src.battle.effects.fade_effect import FadeEffect


class EffectManager(object):

    def __init__(self, state):

        self.state = state

        self.effects = []

    def add_effect(self, effect):

        self.effects.append(effect)

    def remove_effect(self, effect):

        self.effects.remove(effect)

    def run(self):

        for effect in self.effects:
            effect.run()

    def draw(self, surface):

        for effect in self.effects:
            effect.draw(surface)

    def fade_unit(self, unit, battle_line):
        fade = FadeEffect(self, unit, battle_line)
        self.add_effect(fade)

    def flash_unit(self, unit, hits, battle_line):
        flash = FlashEffect(self, unit, battle_line, hits)
        self.add_effect(flash)



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

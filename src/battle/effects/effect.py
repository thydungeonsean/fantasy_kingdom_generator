

class Effect(object):

    def __init__(self, manager):

        self.effect_manager = manager

    def end_effect(self):

        self.effect_manager.remove_effect(self)

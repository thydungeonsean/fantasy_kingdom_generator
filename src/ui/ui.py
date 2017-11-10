from state_template.main_menu_template import MainMenuUI
from state_template.in_game_menu_template import InGameMenuUI


class UI(object):

    @classmethod
    def create_main_menu_ui(cls, state):
        ui = cls(state)

        MainMenuUI(state, ui).add_to_state()

        return ui

    @classmethod
    def create_in_game_menu_ui(cls, state):
        ui = cls(state)
        InGameMenuUI(state, ui).add_to_state()
        return ui

    @classmethod
    def create_nation_choose_ui(cls, state):
        ui = cls(state)

        return ui

    @classmethod
    def create_strategic_mode_ui(cls, state):

        ui = cls(state)

        return ui

    @classmethod
    def create_battle_mode_ui(cls, state):

        ui = cls(state)

        return ui

    def __init__(self, state):

        self.state = state
        self.elements = []
        self.key_element_dict = {}

    def add_element(self, element):
        self.elements.append(element)
        element.set_ui(self)

    def remove_element(self, element):
        self.elements.remove(element)

    def add_key_element(self, element, key):
        self.key_element_dict[key] = element
        self.elements.append(element)

    def remove_key_element(self, key):
        element = self.key_element_dict.get(key, None)
        if element is None:
            raise Exception('trying to remove non existant key element from ui')
        self.remove_element(element)
        del self.key_element_dict[key]

    def click(self, point):
        for element in self.elements:
            clicked = element.click(point)
            if clicked:
                return True
        return False

    def run(self):
        for element in self.elements:
            element.run()

    def draw(self, surface):
        for element in self.elements:
            element.draw(surface)

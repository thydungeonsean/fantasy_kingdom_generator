from state_template.main_menu_template import MainMenuUI


class UI(object):

    @classmethod
    def create_main_menu_ui(cls, state):
        ui = cls(state)

        MainMenuUI(state, ui).add_to_state()

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

    def add_element(self, element):
        self.elements.append(element)
        element.set_ui(self)

    def remove_element(self, element):
        self.elements.remove(element)

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

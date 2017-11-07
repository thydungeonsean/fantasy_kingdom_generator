class UI(object):

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

from building import Building
from src.constants import SETTLEMENT


class Settlement(Building):

    def __init__(self, nation, coord, image_key=SETTLEMENT):

        Building.__init__(self, nation, coord, 'settlement', image_key=image_key)

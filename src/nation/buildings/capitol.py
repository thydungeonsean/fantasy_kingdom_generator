from settlement import Settlement
from src.constants import CAPITOL


class Capitol(Settlement):

    def __init__(self, nation, coord):

        Settlement.__init__(self, nation, coord, image_key=CAPITOL)

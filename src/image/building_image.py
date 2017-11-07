from map_object_image import MapObjectImage
import pygame


class BuildingImage(MapObjectImage):

    BASE_COLOR = (125, 125, 125)

    def __init__(self, key, color, owner):

        MapObjectImage.__init__(self, key, owner)

        self.color = BuildingImage.BASE_COLOR
        self.recolor_image(color)

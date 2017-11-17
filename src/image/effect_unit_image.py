from unit_image import UnitImage


class EffectUnitImage(UnitImage):

    FLASH_COLOR = (250, 250, 250)

    def __init__(self, unit, mode='flash'):

        unit_image = unit.image
        UnitImage.__init__(self, unit_image.key, self.set_start_color(unit, mode))
        self.base_image = unit_image
        self.image_coord = unit.image_coord

        self.alpha = 255

    def fade(self, amt):
        self.alpha -= amt
        self.apply_alpha(self.alpha)

    def set_start_color(self, unit, mode):

        if mode == 'flash':
            return EffectUnitImage.FLASH_COLOR
        elif mode == 'fade':
            return unit.image.color

    def apply_alpha(self, amt):

        for image in self.frames.itervalues():
            image.set_alpha(amt)

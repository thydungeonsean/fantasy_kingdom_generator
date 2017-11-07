from src.constants import *
from image import Image
import pygame


class ImageCache(object):

    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = cls()
        return cls.instance
        
    def __init__(self):
    
        self.cache = {}
        
    def get_image(self, key):
    
        if self.cache.get(key, None) is None:
            self.load_image(key)
        return self.cache.get(key)
        
    def load_image(self, key):
        
        image = Image(key)
        self.cache[key] = image

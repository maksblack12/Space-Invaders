import pygame

class ImageManager:
    def __init__(self):
        self.loadedImages={}

    def get(self, name):
        if name in self.loadedImages:
            return self.loadedImages[name]
        img=pygame.image.load(f"rsrc/image/{name}.png")
        self.loadedImages[name]=img
        return img


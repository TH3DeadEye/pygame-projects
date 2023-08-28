import pygame

BASE_IMG_PATH = '/Users/arman/Desktop/Folders/Programming/python/project/pygame/pygamePlatformer-DafluffyPotato/data/images/'

def load_image(path):
    img = pygame.image.load(BASE_IMG_PATH + path).convert()
    img.set_colorkey((0,0,0))

    return img
    

#/Users/arman/Desktop/Folders/Programming/python/project/pygame/pygamePlatformer-DafluffyPotato/data/images/entities/player.png
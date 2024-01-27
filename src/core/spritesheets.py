import pygame
from src.core.functions import *

class Spritebatch:
    def __init__(self,FILE,colorkey):
        self.sheet = load_image(FILE,alpha=True)
        self.colorkey = colorkey
        self.hashtable = {}
    def image_at(self,x,y,dx,dy):
        hsh = str(x)+str(y)+str(dx)+str(dy)
        try:
            img = self.hashtable[hsh]
            return img
        except KeyError:
            print("Nuevo pedazo de batch")
            rect = pygame.Rect((x,y,dx,dy))
            image = pygame.Surface(rect.size).convert()
            image.blit(self.sheet,(0,0),rect)
            if(self.colorkey != None):
                image.set_colorkey(self.colorkey,pygame.RLEACCEL)
            self.hashtable[hsh] = image
            return image

import pygame
from src.core.Char import *

class Fruta(Char):
    def __init__(self,W,H,nombre,puntos):
        super().__init__(W,H,nombre,1)
        self.Puntos = puntos
        self.Afiliacion = None
        

    def LoadSheet(self,image,W,H):
        arr = []
        for h in range(H):
            for w in range(W):
                print(str(w)+","+str(h))
                arr.append(image.image_at(w*self.rect.width,h*self.rect.height,self.rect.width,self.rect.height))
        self.set_images(arr);
        self.set_anim("idle",[0,0,0,0])

    def Kill(self):
        self.kill();

    def update(self,*args):
        self.update_internals();

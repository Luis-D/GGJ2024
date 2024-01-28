import pygame
from src.core.Char import *
from assets.base.soundplayer import SoundPlayer

class chiste(Char):
    def __init__(self,W,H,nombre,cam):
        super().__init__(W,H,nombre,nombre)
        self.timer = 0;
        self.x = 100000
        self.cam = cam

    def update(self):
        self.update_internals_pre()
        self.y = self.cam.getUpperBorder()
        if(self.timer > 0):
            self.x = self.cam.getLeftBorder()

            self.timer -=1
        else:
            self.x=100000
        self.update_internals_pos()

    def spawn(self,imago):
        SoundPlayer.pooling("assets/sounds/boom.ogg")
        
        self.load_Sheet(imago,1,1);
        self.timer = 45

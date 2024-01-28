from src.core.Inputs import *
from src.core.Char import *
from src.core.spritesheets import *
from assets.base.soundplayer import SoundPlayer
import random

class plataformaMini(Char):
    def __init__(self,W,H,nombre,Factor,Lista, padre):
        super().__init__(W,H,nombre,"Factor")
        self.Factor = Factor
        self.padre = padre
        self.collider = True
        self.broken = False
        self.Lista = Lista
        self.vidrio = Spritebatch("assets/sprites/vidrio.png",(0,0,0))
        self.trampolin = Spritebatch("assets/sprites/plataforma.png",(0,0,0))
        self.vidrio_roto = Spritebatch("assets/sprites/plataforma.png",(0,0,0))

    def VSChar(self,char):
        if char.gy + char.salto <= 0:
            return False
        c = self.rect.colliderect(char.rect)
        return c

    def update(self):
        self.update_internals_pre()
        for J in self.Lista:
            if self.VSChar(J):
                if self.collider == False:
                    if self.broken == True:
                        break
                J.set_salto(self.Factor)
                self.play_sound()
        self.update_internals_pos()

    def play_sound(self):
        if self.collider == False:
            num = random.randint(1,2)
            if num == 1:
                SoundPlayer.pooling(ASSETS_DIR+"sounds/platform/glass1.ogg")
            else:
                SoundPlayer.pooling(ASSETS_DIR+"sounds/platform/glass2.ogg")
            # CARGAR EL SPRITE DE VIDRIO ROTO AQUI
            self.padre.imagen.load_Sheet(self.vidrio_roto,4,8)
            self.broken = True
            pass
        else:
            if self.Factor == 8:
                SoundPlayer.pooling(ASSETS_DIR+"sounds/platform/boing.ogg")
                pass

class plataforma(Char):

    def update_fisico_pos(self):
        self.factor.x =  self.imagen.x
        self.factor.y = self.imagen.y
        self.factor.update_internals_pos()
        self.imagen.update_internals_pos()

    def __init__(self,W,H,x,y,nombre,Factor,Lista,sprite,spritesheet_h,spritesheet_w):
        self.imagen = plataformaMini(W,H,nombre,Factor,[], self)
        self.spritesheet_h = spritesheet_h
        self.spritesheet_w = spritesheet_w
        self.factor = plataformaMini(W,H,nombre,Factor,Lista, self)
        self.imagen.load_Sheet(sprite,spritesheet_h,spritesheet_w)
        self.imagen.x = x
        self.imagen.y = y

    def setRandomAttr(self):
        numero = random.randint(0,100)
        self.factor.collider = True
        self.factor.broken = False
        self.factor.Factor = 4
        if numero > 60 and numero < 90:
            self.factor.Factor = 8
            # CARGAR EL SPRITE DE TRAMPOLIN AQUI
            self.imagen.load_Sheet(self.factor.trampolin,self.spritesheet_h,self.spritesheet_w)

        elif numero >= 90:
            self.factor.collider = False
            # CARGAR EL SPRITE DE VIDRIO AQUI
            self.imagen.load_Sheet(self.factor.vidrio,self.spritesheet_h,self.spritesheet_w)

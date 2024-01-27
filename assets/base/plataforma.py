from src.core.Inputs import *
from src.core.Char import *

class plataformaMini(Char):
    def __init__(self,W,H,nombre,Factor,Lista):
        super().__init__(W,H,nombre,"Factor")
        self.Factor = Factor
        self.Lista = Lista

    def VSChar(self,char):
        if((char.gy+char.salto)<=0):
            return False;
        c = self.rect.colliderect(char.rect);
#        print(self.rect,char.rect,c);
        return c;

    def update(self):
        self.update_internals_pre()
        for J in self.Lista:
            if (self.VSChar(J)):
                J.set_salto(self.Factor)
        self.update_internals_pos()


class plataforma(Char):

    def update_fisico_pos(self):
        self.factor.x =  self.imagen.x
        self.factor.y = self.imagen.y
        self.factor.update_internals_pos()
        self.imagen.update_internals_pos()

    def __init__(self,W,H,x,y,nombre,Factor,Lista,sprite,spritesheet_h,spritesheet_w):
        self.imagen = plataformaMini(W,H,nombre,Factor,[])
        self.factor = plataformaMini(W,H,nombre,Factor,Lista)
        self.imagen.load_Sheet(sprite,spritesheet_h,spritesheet_w)
        self.imagen.x = x
        self.imagen.y = y
        

 


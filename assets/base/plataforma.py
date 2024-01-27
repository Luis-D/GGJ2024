from src.core.Inputs import *
from src.core.Char import *

class plataforma(Char):
    def __init__(self,W,H,nombre,Factor,Lista):
        super().__init__(W,H,nombre,"Factor")
        self.Factor = Factor;
        self.Lista = Lista;

    def VSChar(self,char):
        c = self.rect.colliderect(char.rect);
        print(self.rect,char.rect,c);
        return c;

    def update(self):
        self.update_internals_pre()
        for J in self.Lista:
            if(self.VSChar(J)):
                J.set_salto(self.Factor)
        self.update_internals_pos()

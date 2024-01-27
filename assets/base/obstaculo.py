from src.core.Char import *

class obstacGenerico(Char):

    def __init__(self,W,H,nombre,Factor,Lista,Acc):
        super().__init__(W,H,nombre,"nombre");
        self.Factor = Factor
        self.Lista = Lista
        self.Acc = Acc

    def VSChar(self,char):
        if((char.gy+char.salto)<=0):
            return False;
        c = self.rect.colliderect(char.rect);
#        print(self.rect,char.rect,c);
        return c;


    def update(self):
        self.update_internals_pre();
        self.vecy = Factor
        for P in Lista:
            if(VSChar(P)):
                self.Acc(P);
        self.update_internals_pos();

class obstacChiste(obstacGenerico):

    def Acc(Char):
        Char.puntuacion+=100;

    def __init__(self,W,H,nombre,Factor,Lista):
        super().__init__(self,W,H,nombre,Factor,Lista,self.Acc);


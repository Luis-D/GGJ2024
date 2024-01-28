from src.core.Char import *
import random

class obstacGenerico(Char):

    def __init__(self,W,H,nombre,Factor,Lista,Acc):
        super().__init__(W,H,nombre,"nombre");
        self.Factor = Factor
        self.Lista = Lista
        self.Acc = Acc
        self.accel_timer = 0
        self.gravedad = 0.5

    def VSChar(self,char):
        c = self.rect.colliderect(char.rect);
#        print(self.rect,char.rect,c);
        return c;


    def update(self):
        self.update_internals_pre();
        self.vecy = self.Factor*self.accel_timer*self.gravedad;
        for P in self.Lista:
            if(self.VSChar(P)):
                self.Acc(P);
        self.accel_timer += 0.2
        self.update_internals_pos();

class obstacChiste(obstacGenerico):

    def Acc(self,Char):
        self.chistaco.spawn(self.ListaSprites[random.randint(0,len(self.ListaSprites)-1)]);

    def __init__(self,W,H,nombre,Factor,Lista,chistaco,ListaSprites):
        super().__init__(W,H,nombre,Factor,Lista,self.Acc)
        self.chistaco = chistaco
        self.ListaSprites = ListaSprites;


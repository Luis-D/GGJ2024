from src.core.Inputs import *
from src.core.Char import *

class PJ(Char):

    def __init__(self,W,H,nombre):
        self.gravedad = 0.5
        self.mov_speed = 1
        self.accel_timer = 0;
        self.altitud = 0;
        self.puntuacion = 0;

    def set_salto(self,factor):
        self.vecy -= factor
        self.accel_timer = 0

    def update(self):
        self.update_internals_pre();
        self.puntuacion += (-self.vecy);

        if(Controles.der):
            self.vecx+=self.mov_speed;
        if(Controles.izq):
            self.vecx-=self.mov_speed

        self.vecy = (self.vecy)+(self.accel_timer*self.gravedad);

        self.update_internals_pos();

        self.accel_timer +=0.2; 

        self.updateAnim();

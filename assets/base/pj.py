from src.core.Inputs import *
from src.core.Char import *

class PJ(Char):

    def __init__(self,W,H,nombre):
        super().__init__(W,H,nombre,"PJ");
        self.gravedad = 0.5
        self.mov_speed = 4
        self.accel_timer = 0;
        self.altitud = 0;
        self.puntuacion = 0;
        self.salto = 0;
        self.gy = 0;
        self.maxy = 0;

    def set_salto(self,factor):
        self.salto = -factor
        self.accel_timer = 0
        self.gy = 0;
        if self.cur_anim[-1] == "R":
            self.cur_anim = "SaltoR"
        else:
            self.cur_anim = "SaltoL"
        

    def update(self):
        if(Controles.der):
            self.vecx+=self.mov_speed;
            self.cur_anim = "CaminataR"
        if(Controles.izq):
            self.vecx-=self.mov_speed
            self.cur_anim = "CaminataL"

        self.update_internals_pre();


        self.gy = (self.accel_timer*self.gravedad);
        self.vecy = self.gy + self.salto;
        if(self.vecy<0):
            if((self.y+self.vecy) < self.maxy):
                self.maxy=self.y+self.vecy
                self.puntuacion-=round(self.vecy);
                if self.cur_anim[-1] == "R":
                    self.cur_anim = "SonicR"
                else:
                    self.cur_anim = "SonicL"
        else:
            if self.cur_anim[-1] == "R":
                self.cur_anim = "CaidaR"
            else:
                self.cur_anim = "CaidaL"

        self.update_internals_pos();

        self.accel_timer +=0.2; 

        self.updateAnim();


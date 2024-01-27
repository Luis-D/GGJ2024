from src.core.Char import *
from assets.base.soundplayer import SoundPlayer
import random

class Macaco(Char):

    def __init__(self,W,H,nombre,Afiliacion=1,Ataque=25/60,Vida=100,Tipo=0,Sexo=0,raza='monk',mute=False):
        super().__init__(W,H,nombre,Tipo);
        self.Afiliacion=1
        self.mov_speed = 1;
        self.ia_counter = 0;
        self.target = None;
        self.target_x = None;
        self.ia_state = 2;
        self.ia_mind = 0;
        self.Vida=Vida
        self.Ataque = Ataque
        self.Sexo = Sexo
        self.mute = mute
        self.raza = raza

    def Atacar(self,objetivo):
        torpeza = random.randint(0,3-self.Afiliacion)
        if torpeza == 0:
            objetivo.Vida = objetivo.Vida - (self.Ataque)
            if(self.ia_mind != 2):
                self.ia_mind =2
                rand_sound = random.randint(0,90)
                if self.mute == False:
                    if rand_sound <= 30:
                        SoundPlayer.pooling(ASSETS_DIR+"sounds/interactions/punch1.ogg",0.2)
                    elif rand_sound <= 60:
                        SoundPlayer.pooling(ASSETS_DIR+"sounds/interactions/punch2.ogg",0.2)
                    elif rand_sound <= 90:
                        SoundPlayer.pooling(ASSETS_DIR+"sounds/interactions/punch3.ogg",0.2)
                    if rand_sound <= 30:
                        SoundPlayer.pooling(ASSETS_DIR+"sounds/"+self.raza+"/hostile1.ogg")
                    elif rand_sound <= 60:
                        SoundPlayer.pooling(ASSETS_DIR+"sounds/"+self.raza+"/hostile2.ogg")
                    elif rand_sound <= 90:
                        SoundPlayer.pooling(ASSETS_DIR+"sounds/"+self.raza+"/hostile3.ogg")
                    rand_sound = random.randint(0,90)

    def LoadSheet(self,image,W,H):
        arr = []
        for h in range(H):
            for w in range(W):
                print(str(w)+","+str(h))
                arr.append(image.image_at(w*self.rect.width,h*self.rect.height,self.rect.width,self.rect.height))
        self.set_images(arr);

        self.set_anim("idle",[0,0,0,0])
        self.set_anim("izq",[8,9,10,11])
        self.set_anim("der",[24,25,26,27])

    def CheckMuerte(self):   
        if(self.Vida <=0):
            if self.mute == False:
                rand_sound = random.randint(0,90)
                if rand_sound <= 30:
                    SoundPlayer.pooling(ASSETS_DIR+"sounds/"+self.raza+"/death1.ogg")
                elif rand_sound <= 60:
                    SoundPlayer.pooling(ASSETS_DIR+"sounds/"+self.raza+"/death2.ogg")
                elif rand_sound <= 90:
                    SoundPlayer.pooling(ASSETS_DIR+"sounds/"+self.raza+"/death3.ogg")
                self.kill()
        pass
   
    def updateAnim(self):
        if(self.vecx > 0):
            self.cur_anim = "der"
        if(self.vecx < 0):
            self.cur_anim = "izq"

    def update(self,*args):
        self.update_internals();
        self.CheckMuerte();
        
        if(self.ia_state == 0):
            print(self.nombre + " en 0")
            self.target_x = self.x+(16*random.randint(-50,+(50)))
            self.ia_counter=60*4;
            self.ia_state = 1;
            self.ia_mind = 0;
        elif(self.ia_state ==1):
            print(self.nombre + " en 1")
            if(self.target_x == None):
                print("AAAAAAH")
                self.ia_state = 0;
                return
            if(self.target_x > self.x):
                self.vecx = self.mov_speed;
            else:
                self.vecx =-self.mov_speed;
            if((abs((self.vecx+self.x)-self.target_x)<=self.mov_speed) or (self.ia_counter <= 0)):
                print("En objetivo: "+str(self.target_x)+" "+str(self.x))
                self.vecx = 0;
                self.vecy = 0;
                self.ia_counter=0;
                self.ia_state = 2;
                return

            self.ia_counter = self.ia_counter -1;
            self.ia_state = 2;
        elif(self.ia_state == 2):
            print("En 2")
            obj = False
            #Chequear qué otros changos hay cerca
            for g in self.groups():
                for s in g.sprites():
                    if((s.Tipo==0)):
                        if(abs(self.x-s.x)<(16*5)):
                            

                            if(s.Afiliacion == 0):
                                print("VER AL CHANGO") 
                                obj = True                     
                                self.target_x = s.x;
                                self.ia_counter = 60

                            if((self.Afiliacion==2) and (s.Afiliacion != 2)):                            
                                if(abs(self.x-s.x)<(20)):
                                    print("VER A OTRO CHANGO") 
                                    obj = True
                                    print("AL ATAQUE")
                                    self.Atacar(s)
                            else:
                                if(self.ia_mind != 1):
                                    self.ia_mind =1
                                    if self.mute == False:
                                        rand_sound = random.randint(0,90)
                                        if rand_sound <= 30:
                                            SoundPlayer.pooling(ASSETS_DIR+"sounds/"+self.raza+"/seek1.ogg")
                                        elif rand_sound <= 60:
                                            SoundPlayer.pooling(ASSETS_DIR+"sounds/"+self.raza+"/seek2.ogg")
                                        elif rand_sound <= 90:
                                            SoundPlayer.pooling(ASSETS_DIR+"sounds/"+self.raza+"/seek3.ogg")

            if((self.x<=Global.Boundary_X_Min)):
                self.target_x = random.randint(self.x,self.x+10)
                self.ia_counter = 60
                self.ia_mind=0
                self.ia_state = 1
                print("Colision")
            if((self.x>=Global.Boundary_X_Max-self.rect.width)):
                self.target_x = random.randint(self.x-10,self.x)
                self.ia_counter = 60
                self.ia_state = 1
                self.ia_mind=0
                print("Colision")

            print("obj "+str(obj))

            if(self.ia_counter<=0 and obj==False):
                self.ia_state=0
                return
            
            self.ia_state=1

        self.updateAnim();
        

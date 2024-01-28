import pygame
from src.core.globalscope import *

from src.core.functions import *
from src.core.constants import *
from src.core.spritesheets import *
import math
from src.core.Inputs import *
import random

from assets.base.soundplayer import SoundPlayer
from src.core.Cam import *
from assets.base.pj import *
from assets.base.plataforma import *
from assets.base.obstaculo import *
from assets.base.chiste import *
from assets.base.allObjects import *

# variables globales
score = 0
contador = 0
xxcounter = 0
pcounter = 1
plataformas = []
List = CharList() 


mono = PJ(64,89,"chango")
spri = Spritebatch("assets/sprites/player/stickman.png",(255,255,255))
sprig = Spritebatch("assets/sprites/player/playergray.png",(0,0,0))
mono.load_Sheet(spri,7,4)
mono.set_anim("CaminataR",[1,2,5,6])
mono.set_anim("CaminataL",[7,8,11,12])
mono.set_anim("SaltoR",[3,4,5])
mono.set_anim("SaltoL",[9,10,11])
mono.set_anim("CaidaR",[4,5,6])
mono.set_anim("CaidaL",[10,11,12])
plataforma1 = plataforma(64,2,0,0,"p",5,[mono],spri,4,8)
List.Lista.append(mono)
List.Lista.append(plataforma1.imagen)

# Definiciòn #


# marcador de score
font = pygame.font.Font(None, 36)

# Función para mostrar el marcador en la pantalla
def show_score(score):
    score_text = font.render("Puntuación: {}".format(mono.puntuacion), True, (255, 255, 255))
    Global.screen.blit(score_text, (10, 10))

for i in range(4):
    p = plataforma(64,2,random.randint(1, 256),-(60*i),"p",5,[mono],spri,4,8)
    plataformas.append(p)
    List.Lista.append(p.imagen)

cam = Cam(0,0,480,320)

chistaco = chiste(Global.W,Global.H,"Chiste",cam)

fruta = obstacChiste(16,16,"chiste",1,[mono],chistaco,[spri])
fruta.load_Sheet(sprig,4,8)
List.Lista.append(fruta)


RenderGroup = pygame.sprite.Group()
RenderGroupP = pygame.sprite.Group()
RenderGroup.add(mono)
RenderGroup.add(fruta)


# RENDERIZADO DE PLATAFORMAS
plataforma1.update_fisico_pos()
RenderGroup.add(plataforma1.imagen)
RenderGroup.add(chistaco)
RenderGroupP.add(plataforma1.factor)

for plat in plataformas:
    plat.update_fisico_pos()
    RenderGroup.add(plat.imagen)
    RenderGroupP.add(plat.factor)
    List.Lista.append(plat.imagen)



def funcInfinito(self,Obj,x):
    Obj.y+=x

chistaco.spawn(spri)

def Draw(self):
    cam.surface.fill((0,50,200))
    RenderGroup.draw(cam)
    Global.screen.blit(cam.getSubSurface(),(0,0))
    # Mostrar el marcador en la pantalla
    show_score(score)

def Update(self):
    global pcounter
    global xxcounter
    global score  # Asegúrate de que la variable score esté definida globalmente

    print(cam.getLowerBorder())
    RenderGroup.update()
    RenderGroupP.update()
    pcounter -= 1
    for plat in  plataformas:
        if (plat.imagen.y >= cam.getLowerBorder()):
            pcounter=1
            xx =  random.randint(16, 256-64-32)
            rand = random.randint(1,100)


            plat.imagen.y, plat.imagen.x = cam.getUpperBorder(),xx
            
        plat.update_fisico_pos()

    print("->",cam.getLowerBorder(),cam.y,(Global.H/2)+(cam.h/2))
        
    if mono.y < (cam.getLowerBorder()-(cam.h/2)):
        cam.LookAt(128,mono.y)
        List.applyFunc(funcInfinito,(cam.getLowerBorder()-(cam.h/2)-mono.y))

    if(Controles.esc == True):
        sys.exit()



def Init():
#    SoundPlayer.pooling(ASSETS_DIR+"sounds/menu.ogg")    
    pygame.event.wait()
    Global.timer = 120
    Global.Draw = Draw
    Global.Update = Update
    Global.height_t = 0
    Global.height_tt = 0
    Global.width_t = 0

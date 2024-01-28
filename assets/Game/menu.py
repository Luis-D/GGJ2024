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
from assets.base.allObjects import *

contador = 0

plataformas = []
List = CharList() 


mono = PJ(90,100,"chango")
spri = Spritebatch("assets/sprites/player/stickman.png",(0,0,0))
sprig = Spritebatch("assets/sprites/player/playergray.png",(0,0,0))
print(spri)
mono.load_Sheet(spri,4,8)
plataforma1 = plataforma(64,2,0,0,"p",5,[mono],spri,4,8)

List.Lista.append(mono)
List.Lista.append(plataforma1.imagen)

for i in range(4):
    p = plataforma(64,2,random.randint(1, 256),-(60*i),"p",5,[mono],spri,4,8)
    plataformas.append(p)
    List.Lista.append(p.imagen)

fruta = obstacChiste(16,16,"chiste",1,[mono])
fruta.load_Sheet(sprig,4,8)
List.Lista.append(fruta)

cam = Cam(0,0,256,240)

RenderGroup = pygame.sprite.Group()
RenderGroupP = pygame.sprite.Group()
RenderGroup.add(mono)
RenderGroup.add(fruta)

# RENDERIZADO DE PLATAFORMAS

plataforma1.update_fisico_pos()
RenderGroup.add(plataforma1.imagen)
RenderGroupP.add(plataforma1.factor)

for plat in plataformas:
    plat.update_fisico_pos()
    RenderGroup.add(plat.imagen)
    RenderGroupP.add(plat.factor)
    List.Lista.append(plat.imagen)


def funcInfinito(self,Obj,x):
    Obj.y+=x


def Draw(self):
    cam.surface.fill((0,50,200))
    RenderGroup.draw(cam)
    Global.screen.blit(cam.getSubSurface(),(0,0))

xxcounter = 0
pcounter = 1

def Update(self):
    global pcounter
    global xxcounter
    print(cam.getLowerBorder())
    RenderGroup.update()
    RenderGroupP.update()
    pcounter -= 1
    for plat in  plataformas:
        if (plat.imagen.y >= cam.getLowerBorder()):
            pcounter=1
            print("sdsdss")
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

import pygame
from src.core.globalscope import *

from src.core.functions import *
from src.core.constants import *
from src.core.spritesheets import *
from src.core.Inputs import *
import random

from assets.base.soundplayer import SoundPlayer
from src.core.Cam import *
from assets.base.pj import *
from assets.base.plataforma import *

contador = 0

plataformas = []

mono = PJ(16,16,"chango")
spri = Spritebatch("assets/sprites/player/player.png",(0,0,0))
plataforma1 = plataforma(256,2,0,100,"p",5,[mono],spri,4,8)

for i in range(10):
    plataformas.append(plataforma(64,2,random.randint(1, 256),random.randint(-1000, -120),"p",5,[mono],spri,4,8))
    mono.load_Sheet(spri,4,8)

cam = Cam(0,0,256,240)

RenderGroup = pygame.sprite.Group()
RenderGroupP = pygame.sprite.Group()
RenderGroup.add(mono)

# RENDERIZADO DE PLATAFORMAS

plataforma1.update_fisico_pos()
RenderGroup.add(plataforma1.imagen)
RenderGroupP.add(plataforma1.factor)

for plat in plataformas:
    plat.update_fisico_pos()
    RenderGroup.add(plat.imagen)
    RenderGroupP.add(plat.factor)

def Draw(self):
    cam.surface.fill((0,50,200))
    RenderGroup.draw(cam)
    Global.screen.blit(cam.getSubSurface(),(0,0))

def Update(self):
    RenderGroup.update()
    RenderGroupP.update()
    for plat in  plataformas:
        plat.imagen.y = plat.imagen.y + 1
        if plat.factor.y >= 140:
            numero = random.randint(-500, -120)
            plat.imagen.y, plat.imagen.x = numero, random.randint(1, 256)
            
        plat.update_fisico_pos()
    cam.LookAt(128,0)
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

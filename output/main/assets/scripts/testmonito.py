import pygame
from src.core.globalscope import *
from pygame.locals import *
from src.core.functions import *
from src.core.constants import *
from src.core.spritesheets import *
from src.core.Inputs import *
from src.core.Char import *
import sys
from src.core.Cam import *
from assets.base.mandril import *
from assets.base.player import *

print("Si")
#screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
spri = Spritebatch(ASSETS_DIR+"sprites/player/player.png",(0,0,0));

fondo=Spritebatch(ASSETS_DIR+"/levels/level.png",None).image_at(0,0,1600,256);

RenderGroup = pygame.sprite.Group()

pj = Player(16,16,"Jugador")
pj.set_images([spri.image_at(0,0,16,16),spri.image_at(0,16*2,16,16),spri.image_at(0,16*6,16,16)])
pj.set_anim("test",[0,1,2])
pj.y = 178
RenderGroup.add(pj)

Monito = Macaco(16,16,"Bot",0)
Monito.set_images([spri.image_at(0,0,16,16),spri.image_at(0,16*2,16,16),spri.image_at(0,16*6,16,16)])
Monito.set_anim("test",[0,1,2])
Monito.y = 178
RenderGroup.add(Monito)


print("Si")
camera = Cam(0,0,256,240)

def Update(self):
    camera.LookAt(pj.x+6,pj.y-58)


    RenderGroup.update();


def Draw(self):
    camera.surface.fill((0,0,0))
    camera.blit(fondo,Rect(0,0,1600,256))
    RenderGroup.draw(camera)

   


    Global.screen.blit(camera.getSubSurface(),(0,0));

def Init():
    Global.Update = Update
    Global.Draw = Draw

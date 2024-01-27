import pygame
from src.core.globalscope import *

from src.core.functions import *
from src.core.constants import *
from src.core.spritesheets import *
from src.core.Inputs import *

from assets.base.soundplayer import SoundPlayer
from src.core.Cam import *
from assets.base.pj import *
from assets.base.plataforma import *

contador = 0;

mono = PJ(16,16,"chango")
spri = Spritebatch("assets/sprites/player/player.png",(0,0,0))
print(spri)
mono.load_Sheet(spri,4,8)
cam = Cam(0,0,256,240)

plat = plataforma(256,2,"p",0,[]);
plat.y = 100
plat.load_Sheet(spri,4,8)
platF = plataforma(64,2,"p",5,[mono]);
platF.y = 100
platF.x = 0
platF.update_internals_pos()


RenderGroup = pygame.sprite.Group();
RenderGroupP = pygame.sprite.Group();
RenderGroup.add(mono);
RenderGroup.add(plat);


RenderGroupP.add(platF);

plat = plataforma(256,2,"p",0,[]);
plat.y = 10
plat.x = 70
plat.load_Sheet(spri,4,8)

platF = plataforma(64,2,"p",5,[mono]);
platF.y = 10
platF.x = 70
platF.update_internals_pos()

RenderGroup.add(plat);
RenderGroupP.add(platF);

def Draw(self):
    cam.surface.fill((0,50,200))
    RenderGroup.draw(cam);
    Global.screen.blit(cam.getSubSurface(),(0,0));
    pass

def Update(self):
    RenderGroup.update();
    RenderGroupP.update();
    cam.LookAt(0,0);
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

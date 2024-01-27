import pygame
from src.core.globalscope import *

from src.core.functions import *
from src.core.constants import *
from src.core.spritesheets import *
from src.core.Inputs import *

from assets.base.soundplayer import SoundPlayer
from src.core.Cam import *
from assets.base.mandril import *
from assets.base.pj import *


contador = 0;

mono = PJ(16,16,"chango")
spri = Spritebatch("assets/sprites/player/player.png",(0,0,0))
print(spri)
mono.load_Sheet(spri,4,8)
cam = Cam(0,0,256,240)
RenderGroup = pygame.sprite.Group();
RenderGroup.add(mono);


def Draw(self):
    cam.surface.fill((0,50,200))
    RenderGroup.draw(cam);
    Global.screen.blit(cam.getSubSurface(),(0,0));
    pass

def Update(self):
    RenderGroup.update();
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

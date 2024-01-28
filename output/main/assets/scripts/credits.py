import pygame
from src.core.globalscope import *
from pygame.locals import *
from src.core.functions import *
from src.core.constants import *
from src.core.spritesheets import *
import random
from src.core.Inputs import *
from src.core.Char import *
import sys
from src.core.Cam import *
from assets.base.mandril import *
from assets.base.player import *
from assets.base.fruta import *
import random


image = pygame.transform.scale(load_image(ASSETS_DIR+"sprites/credits.png"), (640, 480))

camera = Cam(0,0,640,480)

def Draw(self):
    camera.surface.fill((0,0,0))
    camera.surface.blit(image,(363,144))
    Global.screen.blit(camera.getSubSurface(),(0,0))

def Update(self):
    if(Controles.esc == True):
        Destroy(None)
        Global.Init(MENU_ARGM)
        
    

def Destroy(self):
    SoundPlayer.stop_pooling()

def Init():
    SoundPlayer.stop_pooling()
    SoundPlayer.pooling(ASSETS_DIR+"sounds/level.ogg")
    Global.Update = Update
    Global.Draw = Draw
    Global.Destroy = Destroy
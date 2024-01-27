import pygame
from src.core.globalscope import *
from pygame.locals import *
from src.core.functions import *
from src.core.constants import *
from src.core.spritesheets import *
from src.core.Inputs import *
from src.interfaces.menu import *
from assets.base.soundplayer import SoundPlayer
from src.core.Cam import *
from assets.base.mandril import *

import sys


def Draw(self):
    pass

def Update(self):
    if(Controles.esc == True):
        sys.exit()

def Init():
#    SoundPlayer.pooling(ASSETS_DIR+"sounds/menu.ogg")    
    pygame.event.wait()
    Global.timer = 120
    Global.Draw = DrawBG
    Global.Update = Update
    Global.height_t = 0
    Global.height_tt = 0
    Global.width_t = 0

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

img = pygame.transform.scale(load_image(ASSETS_DIR+"sprites/lose1.jpg"), (640, 480))
img1 = pygame.transform.scale(load_image(ASSETS_DIR+"sprites/lose2.jpg"), (640, 480))
img2 = pygame.transform.scale(load_image(ASSETS_DIR+"sprites/lose3.jpg"), (640, 480))

image = None

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
    global image
    SoundPlayer.stop_pooling()
    numero = random.randint(1,3)
    if numero == 1:
        print("1")
        SoundPlayer.pooling(ASSETS_DIR+"sounds/lose1.ogg")
        image = img

    elif numero == 2:
        print("2")
        SoundPlayer.pooling(ASSETS_DIR+"sounds/lose1.ogg")
        image = img1

    elif numero == 3:
        print("3")
        SoundPlayer.pooling(ASSETS_DIR+"sounds/lose1.ogg")
        image = img2
    print("ASDASDASDASD")
    print(numero)
    Global.Update = Update
    Global.Draw = Draw
    Global.Destroy = Destroy
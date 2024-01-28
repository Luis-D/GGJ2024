
import pygame
from src.core.globalscope import *
from pygame.locals import *
from src.core.functions import *
from src.core.constants import *
from src.core.spritesheets import *
from src.core.Inputs import *
import sys

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
spri = Spritebatch("assets/sprites/fondo.jpg",None)

def DrawBG(self):
    spriimg = spri.image_at(0,0,256,256)
    screen.blit(spriimg,(0,0))

def Update(self):
    if(Controles.esc == True):
        sys.exit()

def Init():
    Global.Draw = DrawBG
    Global.Update = Update

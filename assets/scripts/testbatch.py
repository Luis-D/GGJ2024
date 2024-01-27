import pygame
from src.core.globalscope import *
from pygame.locals import *
from src.core.functions import *
from src.core.constants import *
from src.core.spritesheets import *
from src.core.Inputs import *
from src.core.Char import *
import sys

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
spri = Spritebatch("assets/sprites/fondo.jpg",None)

npc = Char(0,0,"Changuito")
npc.set_images([spri.image_at(0,0,256,256),spri.image_at(64,0,256,256)])

RenderGroup = pygame.sprite.Group()
RenderGroup.add(npc)


def Update(self):
    npc.cur_image =0
    if(Controles.der):
        print("lmao")
        npc.cur_image = 1
    npc.update_image()
    npc.update_rect()

def Draw(self):
    screen.fill((0,0,0))
    RenderGroup.draw(screen)


def Init():
    Global.Update = Update
    Global.Draw = Draw

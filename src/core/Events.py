
import sys
import pygame
from pygame.locals import *
from src.core.Inputs import *

def gpad_process(event,cond,boolean):
    if event.type == cond:
        if(event.key == pygame.K_UP):
            Controles.arr = boolean
        if(event.key == pygame.K_DOWN):
            Controles.aba = boolean
        if(event.key == pygame.K_LEFT):
            Controles.izq = boolean
        if(event.key == pygame.K_RIGHT):
            Controles.der = boolean
        if(event.key == pygame.K_SPACE):
            Controles.acc = boolean
        if(event.key == pygame.K_RETURN):
            Controles.acc = boolean
        if(event.key == pygame.K_ESCAPE):
            Controles.esc = boolean
        if(event.key == pygame.K_BACKSPACE):
            Controles.can = boolean
        if(event.key == pygame.K_LCTRL):
            Controles.can = boolean


def E_process():

    for event in pygame.event.get():
        gpad_process(event,pygame.KEYDOWN,True)
        gpad_process(event,pygame.KEYUP,False)
        if event.type == pygame.QUIT:
            print("Muerto")
            sys.exit()




import pygame
from src.core.globalscope import *
from pygame.locals import *
from src.core.functions import *
from src.core.constants import *
from src.core.spritesheets import *
from src.core.Inputs import *
from src.interfaces.menu import *

import sys

def comenzar_nuevo_juego():
    print (" Función que muestra un nuevo juego.")
    mod = importlib.import_module("assets.Game.lvl1")
    mod.Init()
    mod.Update(None)

def mostrar_opciones():
    print (" Función que muestra otro menú de opciones.")

def creditos():
    print (" Función que muestra los creditos del programa.")

def salir_del_programa():
    import sys
    print (" Gracias por utilizar este programa.")
    sys.exit(0)

salir = False
opciones = [
        ("Jugar", comenzar_nuevo_juego),
        ("Opciones", mostrar_opciones),
        ("Creditos", creditos),
        ("Salir", salir_del_programa)
    ]
pygame.font.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
fondo = load_image(ASSETS_DIR+"sprites/fondo.jpg", True).convert()
fondo = pygame.transform.scale(fondo, (SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.mixer.init()
pygame.mixer.music.load(ASSETS_DIR+"sounds/menu.ogg")
menu = Menu(opciones)

def DrawBG(self):
    if Global.width_t < SCREEN_WIDTH:
        Global.width_t = Global.width_t+(Global.W/120)
    if Global.height_t < SCREEN_HEIGHT:
        Global.height_t = Global.height_t+(Global.H/120)
    screen.blit(pygame.transform.scale(fondo, (Global.width_t, Global.height_t)),(0,0))
    if Global.timer == 0:
        menu.imprimir(screen)

def Update(self):
    if(Controles.esc == True):
        sys.exit()
    if Global.timer == 0:
        menu.actualizar()
    else:
        Global.timer = Global.timer-1

def Init():
    pygame.mixer.music.play()
    pygame.event.wait()
    Global.timer = 120
    Global.Draw = DrawBG
    Global.Update = Update

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


def comenzar_nuevo_juego():
    Destroy()
    SoundPlayer.stop_pooling()
    print (" Función que muestra un nuevo juego.")
    mod = importlib.import_module("assets.Game.game")
    importlib.reload(mod)
    mod.Init()
    mod.Update(None)

def mostrar_opciones():
    print (" Función que muestra otro menú de opciones.")

def creditos():
    print (" Función que muestra los creditos del programa.")
    Destroy()
    mod = importlib.import_module(CREDITS_ARGM)
    importlib.reload(mod)
    mod.Init()
    mod.Update(None)

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
fondo = load_image(ASSETS_DIR+"sprites/fondochangorigen.png", True).convert()
fondo = pygame.transform.scale(fondo, (SCREEN_WIDTH, SCREEN_HEIGHT))
logo = load_image(ASSETS_DIR+"logo/logo.png", True)
logo = pygame.transform.scale(logo, (SCREEN_WIDTH, SCREEN_HEIGHT))
#pygame.mixer.music.load(ASSETS_DIR+"sounds/menu.ogg")
menu = Menu(opciones)

camera = Cam(16*15,0,256,240)
RenderGroup = pygame.sprite.Group()

anim2 = False
end = False
fast = 45
def DrawBG(self):
    global anim2
    global end
    global fast
    global fondo
    global logo
    screen.fill((0,0,0))


    if(anim2 and end == False):     
        
        Global.width_t = Global.width_t-(Global.W/80)
        Global.height_t = Global.height_t-(Global.H/80)
        if(Global.width_t <= 0 or Global.height_t <= 0):
            Global.width_t=0
            Global.height_t=0
            anim2=False
            end = True
            fast = 120
            fondo = load_image(ASSETS_DIR+"sprites/WIP Fondo.png", True).convert()
            logo = load_image(ASSETS_DIR+"sprites/logo.png", True)
            fondo = pygame.transform.scale(fondo, (SCREEN_WIDTH, SCREEN_HEIGHT))

    if(anim2==False ):
        Global.width_t = Global.width_t+(Global.W/fast)
        Global.height_t = Global.height_t+(Global.H/fast)
        if(Global.width_t>=SCREEN_WIDTH):
            anim2=True

    screen.blit(pygame.transform.scale(fondo, (Global.width_t, Global.height_t)),(0,0))
    screen.blit(pygame.transform.scale(logo, (SCREEN_WIDTH, Global.height_t)),(0,0))

    if Global.timer == 0:
        menu.imprimir(screen)
    camera.surface.fill((0,0,0))
    RenderGroup.draw(camera)
    sub = camera.getSubSurface()
    sub.set_colorkey((0,0,0))
    screen.blit(sub,(0,0))

def Destroy():
    RenderGroup.empty()

def Update(self):
    RenderGroup.update()
    if(Controles.esc == True):
        sys.exit()
    if Global.timer == 0:
        menu.actualizar()
    else:
        Global.timer = Global.timer-1

def Init():
    global anim2
    global end
    global fast
    global fondo
    global logo
    anim2 = False
    end = False
    fast = 45
    SoundPlayer.pooling(ASSETS_DIR+"sounds/menu.ogg")
    pygame.event.wait()
    Global.timer = 120
    Global.Draw = DrawBG
    Global.Update = Update
    Global.height_t = 0
    Global.height_tt = 0
    Global.width_t = 0
    fondo = load_image(ASSETS_DIR+"sprites/fondochangorigen.png", True).convert()
    logo = load_image(ASSETS_DIR+"logo/logo.png", True)

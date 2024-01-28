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
from assets.base.pj import *
from assets.base.plataforma import *
from assets.base.obstaculo import *
from assets.base.chiste import *
from assets.base.allObjects import *

# variables globales
score = 0
contador = 0
xxcounter = 0
pcounter = 1
plataformas = []
List = CharList()


mono = PJ(64,88,"chango")
spri = Spritebatch("assets/sprites/player/stickman.png",(255,255,255))
sprig = Spritebatch("assets/sprites/player/playergray.png",(0,0,0))
sprip = Spritebatch("assets/sprites/plataforma.png",(0,0,0))
mono.load_Sheet(spri,7,4)
mono.x = 128-33
mono.update_internals_pos()
mono.set_anim("CaminataR",[1,2,5,6])
mono.set_anim("CaminataL",[7,8,11,12])
mono.set_anim("SaltoR",[3,4,5])
mono.set_anim("SaltoL",[9,10,11])
mono.set_anim("CaidaR",[4,5,6])
mono.set_anim("CaidaL",[10,11,12])
mono.set_anim("SonicR",[16,18,20])
mono.set_anim("SonicL",[23,25,27])
plataforma1 = plataforma(64,8,0,0,"p",5,[mono],sprip,4,8)
plataforma1.imagen.x = 128-32
plataforma1.update_fisico_pos()
List.Lista.append(mono)
List.Lista.append(plataforma1.imagen)
List.Lista.append(mono)



# Definiciòn #


# marcador de score
font = pygame.font.Font(None, 36)

# Función para mostrar el marcador en la pantalla
def show_score(score):
    score_text = font.render("Puntuación: {}".format(mono.puntuacion), True, (255, 255, 255))
    Global.screen.blit(score_text, (10, 10))

for i in range(10):
    p = plataforma(64,8,random.randint(64, 300),-(60*i),"p",5,[mono],sprip,4,8)
    plataformas.append(p)
    List.Lista.append(p.imagen)

RenderGroup = pygame.sprite.RenderUpdates()
RenderGroupP = pygame.sprite.Group()
RenderGroupChiste = pygame.sprite.Group()

cam = Cam(0,0,800,600)

chistaco = chiste(640,480,"Chiste",cam)
chistaco.x = 64
chistaco.update_internals_pos()
chistaco.spawn(spri)
chistaco.timer=0
obstacChistes = []

RenderGroupChiste.add(chistaco)

listamemes = [Spritebatch("assets/sprites/akira.png",(255,0,255)),
              Spritebatch("assets/sprites/gatollorando.png",(255,0,255)),
              Spritebatch("assets/sprites/larry4.png",(255,0,255)),
              Spritebatch("assets/sprites/cato.png",(255,0,255)),
              Spritebatch("assets/sprites/cato2.png",(255,0,255)),
              Spritebatch("assets/sprites/mrincreible.png",(255,0,255)),
              Spritebatch("assets/sprites/rock.png",(255,0,255)),
              Spritebatch("assets/sprites/stripper.png",(255,0,255)),
              Spritebatch("assets/sprites/shrek.png",(255,0,255)),
              Spritebatch("assets/sprites/chopper.png",(255,0,255)),
              Spritebatch("assets/sprites/kokudrip.png",(255,0,255))
              ]

for i in range(3):
    t = obstacChiste(16,16,"Chiste",1,[mono],chistaco,listamemes)
    t.y = 100000
    t.update_internals_pos()
    t.load_Sheet(sprig,4,8)
    List.Lista.append(t)
    obstacChistes.append(t)
    RenderGroup.add(t)



RenderGroup.add(mono)

# RENDERIZADO DE PLATAFORMAS
plataforma1.update_fisico_pos()
RenderGroup.add(plataforma1.imagen)
RenderGroupP.add(plataforma1.factor)

for plat in plataformas:
    plat.update_fisico_pos()
    RenderGroup.add(plat.imagen)
    RenderGroupP.add(plat.factor)
    List.Lista.append(plat.imagen)


def funcInfinito(self,Obj,x):
    Obj.y+=x

cieloInicial = [240,220,255]
cieloFactor = 0.9
cieloFinal = [0,20,128]

def Draw(self):
    global cieloInicial
    global cieloFactor
    global cieloFinal
    cam.surface.fill((cieloInicial[0]+((cieloFinal[0]-cieloInicial[0])*cieloFactor),cieloInicial[1]+((cieloFinal[1]-cieloInicial[1])*cieloFactor),cieloInicial[2]+((cieloFinal[2]-cieloInicial[2])*cieloFactor) ))
    RenderGroup.draw(cam)
    RenderGroupChiste.draw(cam)
    Global.screen.blit(cam.getSubSurface(),(0,0))
    # Mostrar el marcador en la pantalla
    show_score(score)
    cieloFactor = (mono.puntuacion/5000)
    if(cieloFactor>1.0):
        cieloFactor = 1.0

def Update(self):
    global listamemes
    global pcounter
    global xxcounter
    global chistaco
    global score  # Asegúrate de que la variable score esté definida globalmente

    if(mono.y > cam.getLowerBorder()):
       mono.y = 100000
    if(mono.x > cam.getRightBorder()):
       mono.x = cam.getLeftBorder()-16
    if(mono.x < cam.getLeftBorder()-mono.w):
       mono.x = cam.getRightBorder()-mono.w

    RenderGroup.update()
    RenderGroupChiste.update()
    RenderGroupP.update()
    pcounter -= 1
    for plat in  plataformas:
        if (plat.imagen.y >= cam.getLowerBorder()):
            pcounter=1
            xx =  random.randint(-300, 500-64-32)
            rand = random.randint(1,100)

            plat.imagen.y, plat.imagen.x = cam.getUpperBorder(),xx
            plat.setRandomAttr()
            
        plat.update_fisico_pos()

#    print("->",cam.getLowerBorder(),cam.y,(Global.H/2)+(cam.h/2))

    for t in obstacChistes:
        if(t.y >= cam.getLowerBorder()):
            t.accel_timer = 0
            t.x = random.randint(-128,cam.w)
            t.y = cam.getUpperBorder()-random.randint(128,360)
        
    if mono.y < (cam.getLowerBorder()-(cam.h/2)):
        cam.LookAt(128,mono.y)
        List.applyFunc(funcInfinito,(cam.getLowerBorder()-(cam.h/2)-mono.y))

    if mono.y> cam.getLowerBorder():
        Global.Init(GAMEOVER_ARGM)

    if(Controles.esc == True):
        sys.exit()

def Init():
    SoundPlayer.pooling(ASSETS_DIR+"sounds/level.ogg")
    pygame.event.wait()
    Global.timer = 120
    Global.Draw = Draw
    Global.Update = Update
    Global.height_t = 0
    Global.height_tt = 0
    Global.width_t = 0

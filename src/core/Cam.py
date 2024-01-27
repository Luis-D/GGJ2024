import pygame
from src.core.globalscope import *

print("Uy")

class Cam:
    def LookAt(self,x,y):
        self.x=x-(Global.W/2);
        self.y=y-(Global.H/2);

    def __init__(self,x,y,w,h):
        self.h = h;
        self.w = w;
        self.LookAt(x,y)
        self.surface = pygame.Surface((Global.W,Global.H))



    def blit(self,image,coord):
        coord.update(coord.x-self.x,coord.y-self.y,coord.width,coord.height)
        self.surface.blit(image,coord); 

    def getSubSurface(self):
        return pygame.transform.scale(self.surface.subsurface(pygame.Rect(((Global.W/2)-(self.w/2),(Global.H/2)-(self.h/2),(self.w),(self.h)))),(Global.W,Global.H));
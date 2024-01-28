import pygame
from src.core.globalscope import *

class Cam:

    def getUpperBorder(self):
        return self.y + (Global.H/2)-(self.h/2)
    
    def getLeftBorder(self):
        return self.x + (Global.W/2)-(self.w/2)
    def getRightBorder(self):
        return self.x + (Global.W/2)+(self.w/2)

    def getLowerBorder(self):
        return self.y + (Global.H/2)+(self.h/2)

    def LookAt(self,x,y):
        self.x=x-(Global.W/2)
        self.y=y-(Global.H/2)

    def __init__(self,x,y,w,h):
        self.h = h
        self.w = w
        self.LookAt(x,y)
        self.surface = pygame.Surface((Global.W,Global.H))



    def blit(self,image,coord,a,b):
        coord.update(coord.x-self.x,coord.y-self.y,coord.width,coord.height)
        self.surface.blit(image,coord); 

    def getSubSurface(self):
        return pygame.transform.scale(self.surface.subsurface(pygame.Rect(((Global.W/2)-(self.w/2),(Global.H/2)-(self.h/2),(self.w),(self.h)))),(Global.W,Global.H));

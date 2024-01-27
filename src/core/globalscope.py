import importlib
import pygame
from src.core.constants import *

class State:

    timer = 120
    width_t = 0
    height_t = 0

    def __init__(self,W,H):
        self.H = H
        self.W =W
        self.Boundary_X_Min=0;
        self.Boundary_X_Max=1600;

    def SetResolution(self,W,H):
        self.H = H
        self.W = W
        print("d")
        self.screen = pygame.display.set_mode((W,H))
        print("e")

    def Destroy(self,placeholder):
        pass

    def Update(self,placeholder):

        pass
    def Draw(self,placeholder):
        pass
    def Init(self,File):
        self.SetResolution(self.W,self.H)
        mod = importlib.import_module(File)
        mod.Init()

Global = State(SCREEN_WIDTH,SCREEN_HEIGHT)
print("Global Init")

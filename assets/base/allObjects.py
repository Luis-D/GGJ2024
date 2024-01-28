from src.core.Char import *

class CharList:
    def __init__(self):
        self.Lista = []

    def applyFunc(self,func,param):
        for x in self.Lista:
            func(self,x,param);

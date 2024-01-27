from src.core.globalscope import *



def lmao(self):
    print("LMAO")

def lmaodraw(self):
    pass

def Init():
    print("LOAD")
    Global.Update = lmao
    Global.Draw = lmaodraw


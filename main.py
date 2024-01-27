
import sys
import pygame
from pygame.locals import *

from src.core.constants import *
from src.core.functions import *
from src.core.globalscope import * 
from src.core.Events import *



def main():
    pygame.init()
    pygame.mixer.set_num_channels(50)
#    pygame.mixer.init()
    #screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(TITLE)
    try:
        Global.Init(sys.argv[1])
    except:
        Global.Init(MENU_ARGM)

    Clock = pygame.time.Clock()

    while True:
        E_process()
        Global.Update(Global)
        Global.Draw(Global)
        pygame.display.flip()
        Clock.tick(60)

if __name__ == "__main__":
    main()

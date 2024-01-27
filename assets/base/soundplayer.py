import pygame as pg
import time

class SoundPlayer():

    def pooling(dir, volume=1.0):
        for i in range(4):
            if not pg.mixer.Channel(i).get_busy():
                pg.mixer.Channel(i).set_volume(volume)
                pg.mixer.Channel(i).play(pg.mixer.Sound(dir))
                break
    def stop_pooling():
        for i in range(16):
            pg.mixer.Channel(i).stop()
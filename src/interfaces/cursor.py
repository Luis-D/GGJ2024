import random
import pygame
from pygame.locals import *
from src.core.functions import *
from src.core.constants import *

class Cursor:

    def __init__(self, x, y, dy):
        self.image = load_image(ASSETS_DIR+'sprites/cursor.png', True)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.y_inicial = y
        self.dy = dy
        self.y = 0
        self.seleccionar(0)

    def actualizar(self):
        self.y += (self.to_y - self.y) / 10.0
        self.rect.y = int(self.y)

    def seleccionar(self, indice):
        self.to_y = self.y_inicial + indice * self.dy

    def imprimir(self, screen):
        screen.blit(self.image, self.rect)
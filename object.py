import os
import random
import math
import pygame
from collisions import collide, handle_vertical_collision
from globals import WIDTH, HEIGHT, PLAYER_VEL
from sprites import flip, load_sprite_sheets
from os import listdir
from os.path import isfile, join

class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, name=None):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.width = width
        self.height = height
        self.name = name

    def draw(self, window, offset_x):
        window.blit(self.image, (self.rect.x - offset_x, self.rect.y))

import pygame
from setting import *
from entity import *
from support import *

class Mob (Entity):
    def __init__ (self, mob_name, pos, groups):

        #setup
        super().__init__(groups)
        self.sprite_type = "mob"

        #graphics
        self.import_graphics(mob_name)
        self.status = "idle"
        self.image = self.animation [self.status][self.frame_index]
        self.rect = self.image.get_rect (topleft = pos)

    def import_graphics (self, name):
        self.animation = {"idle":[], "move":[], "attack":[]}
        main_path = f"./graphics/mob/{name}/"
        for animation in self.animation.keys():
            self.animation[animation] = import_folder(main_path + animation)
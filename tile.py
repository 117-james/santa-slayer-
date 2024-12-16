import pygame
from setting import *

class Tile (pygame.sprite.Sprite):
    def __init__ (self, pos, groups,  sprite_type, surface = pygame.Surface((TILESIZE, TILESIZE))):
        super().__init__(groups)
        self.sprite_type = sprite_type
        self.image = surface
        if sprite_type == "detail":
            self.rect = self.image.get_rect(topleft = (pos [0], pos [1] - TILESIZE))
            self.hitbox = self.rect.inflate(-5, -15)
             
        elif sprite_type == "larger":
            self.rect = self.image.get_rect(bottomleft=(pos[0], pos[1] + TILESIZE))
            self.hitbox = self.rect.inflate(-20, -110)
        else:
            self.rect = self.image.get_rect(topleft = pos)
            self.hitbox = self.rect.inflate(-5, -10) # inflate pega o rect e muda o tamanho.. confia, vai dar profundidade

    
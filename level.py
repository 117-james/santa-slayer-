import pygame
from setting import *
from tile import Tile
from player import Player
from debug import debug
from support import *


class Level:
    # central do jogo inteiro
    def __init__ (self):
        
        # dava pra passar o screen como método de level mas.. melhor pegar o display surface de qualquer parte do código né?
        self.display_surface = pygame.display.get_surface()

        # sprite setup
        self.visible_sprites = YCameraGroup() # visible sprites são aqueles que vão ser desenhados
        self.obstacle_sprites = pygame.sprite.Group() # sprites que colidem com o player

        self.create_map()

    def create_map (self): # eu vou me matar
        layout = {
            "boundary": import_csv_layout("./map/map_FloorBlocks.csv")
        }
        #whenever we create a tile, we will have visible tiles and obstacle tiles // collision
        #for row_index, row in enumerate(WORLD_MAP):
         #   for col_index, col in enumerate(row):
          #      x = col_index * TILESIZE
           #     y = row_index * TILESIZE
            #if col == "x":
             #   Tile((x, y), [self.visible_sprites])
            #if col == "p":
             #   self.player = Player ((400, 300), [self.visible_sprites], self.obstacle_sprites)
        self.player = Player ((400, 300), [self.visible_sprites], self.obstacle_sprites)
    def run (self):

        # atualizando e rodando o jogo
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()

class YCameraGroup (pygame.sprite.Group): # esse grupo de sprite vai funcionar como uma câmera através das coordenadas y
    
    def __init__ (self):

        # setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2() # o truque foi conectar o offset no player

        # chão
        self.floor_surf = pygame.image.load("./graphics/tilemap/map.png").convert()
        self.floor_rect = self.floor_surf.get_rect (topleft = (0, 0))

    def custom_draw(self, player):
        
        # PORRAAAAAAAA
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        #desenhando chão
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf, floor_offset_pos)


        #for sprite in self.sprites():
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit (sprite.image, offset_pos)
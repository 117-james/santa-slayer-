import pygame
from setting import *
from tile import Tile
from player import Player
from debug import debug
from support import *
from random import choice
from player import *
from weapon import *
from ui import *
from mob import *

class Level:
    # central do jogo inteiro
    def __init__ (self):
        
        # dava pra passar o screen como método de level mas.. melhor pegar o display surface de qualquer parte do código né?
        self.display_surface = pygame.display.get_surface()

        # sprite setup
        self.visible_sprites = YCameraGroup() # visible sprites são aqueles que vão ser desenhados
        self.obstacle_sprites = pygame.sprite.Group() # sprites que colidem com o player


        #attack sprite
        self.current_attack = None

        self.create_map()

        # interface
        self.ui = UI()

    def create_map (self): # eu vou me matar
        layouts = {
           "boundary": import_csv_layout("./graphics/tilemap/boundary.csv"),
           "object": import_csv_layout ("./graphics/tilemap/detail.csv"),
           "entities": import_csv_layout ("./graphics/tilemap/entities.csv")
        }

        graphics = {
            "object": import_folder (".graphics/tilemap")
        }
        print (graphics)
        # quando a gente criar um tile, vai ter os visíveis e de obstáculo // collision

        for style, layout in layouts.items():

            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != "-1":
                
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE

                        if style == "boundary":
                            Tile((x, y), [ self.obstacle_sprites], "invisible")

                        if style == "object":
                            # object tile
                            #surf = graphics ["object"][int(col)]
                            #Tile((x, y), [self.visible_sprites, self.obstacle_sprites], "object", surf)
                            pass

                        if style == "entities":
                            if col == "1028":
                                self.player = Player (
                                (x,y), [self.visible_sprites],
                                self.obstacle_sprites,
                                self.create_attack,
                                self.destroy_attack,
                                self.create_magic)
                            else:
                                if col == "1027": mob_name = "snowman"
                                elif col == "1013": mob_name = "gingerbread"
                                elif col == "": mob_name = "krampus"
                                Mob (mob_name, (x,y), [self.visible_sprites], self.obstacle_sprites)

            
        

    def create_attack (self):
        self.current_attack = Weapon(self.player, [self.visible_sprites])

    def create_magic (self, style, strength, cost):
        print(style)
        print(strength)
        print(cost)

    def destroy_attack (self):
        if self.current_attack:
            self.current_attack.kill()
        self.current_attack = None


    def run (self):

        # atualizando e rodando o jogo
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        self.visible_sprites.mob_update(self.player)
        self.ui.display(self.player)

class YCameraGroup (pygame.sprite.Group): # esse grupo de sprite vai funcionar como uma câmera através das coordenadas y
    
    def __init__ (self):

        # setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2() # o truque foi conectar o offset no player

        # chão
        self.floor_surf = pygame.image.load("./graphics/tilemap/map.png").convert() # png do mapa, literalmente
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

    def mob_update(self, player):
        mob_sprites = [sprite for sprite in self.sprites() if hasattr(sprite, "sprite_type") and sprite.sprite_type == "mob"]
        for mob in mob_sprites:
            mob.mob_update(player)
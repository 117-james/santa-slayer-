import pygame
from setting import *

class Player (pygame.sprite.Sprite):


    def __init__ (self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        self.image = pygame.image.load("./graphics/test/santa.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, -16)

        self.direction = pygame.math.Vector2() # vetor x e y
        self.sp = 2 # speed
        self.obstacle_sprites = obstacle_sprites

    def input (self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1 
        else:
            self.direction.y = 0
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1 
        else:
            self.direction.x = 0

    def move (self, sp):
        # então, tive que fazer uns ajustes
        # quando o player movia diagonalmente, a velocidade aumentava, então normalizei a direção
        # basicamente mudando o tamanho do vetor pra 1 
        if self.direction.magnitude()  != 0: # um vetor de 0 não pode ser normalizado
            self.direction = self.direction.normalize()
            # não importa mais qual direção o jogador move, o tamanho do vetor sempre vai ser 1
        self.hitbox.x += self.direction.x * sp
        self.collision ("horizontal")
        self.hitbox.y += self.direction.y * sp
        self.collision ("vertical")
        self.rect.center = self.hitbox.center
        

    def collision (self, direction):
        
        if direction == "horizontal":

            for sprite in self.obstacle_sprites:

                if sprite.hitbox.colliderect(self.hitbox):

                    if self.direction.x > 0: # move pra direita
                        self.hitbox.right = sprite.hitbox.left
                    
                    if self.direction.x < 0:
                        self.hitbox.left = sprite.hitbox.right

        if direction == "vertical":
            
            for sprite in self.obstacle_sprites:

                if sprite.hitbox.colliderect (self.hitbox):

                    if self.direction.y > 0:
                        self.hitbox.bottom = sprite.hitbox.top

                    if self.direction.y < 0:
                        self.hitbox.top = sprite.hitbox.bottom

    def update (self):
        
        self.input()
        self.move(self.sp)
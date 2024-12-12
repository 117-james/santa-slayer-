import pygame
from setting import *
from support import *


class Player (pygame.sprite.Sprite):


    def __init__ (self, pos, groups, obstacle_sprites, create_attack, destroy_attack):
        super().__init__(groups)
        self.image = pygame.image.load("./graphics/player/down_idle/idle_down.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, -16)

        #graphic setup
        self.import_player_asset ()
        self.status = "down"
        self.frame_index = 0
        self.animation_sp = 0.5

        # movement
        self.direction = pygame.math.Vector2() # vetor x e y
        self.attacking = False
        self.attack_cooldown = 400
        self.attack_time = None # criar timer
        self.obstacle_sprites = obstacle_sprites

        #weapon
        self.create_attack = create_attack
        self.destroy_attack = destroy_attack
        self.weapon_index = 0
        self.weapon = list(weapon_data.keys())[self.weapon_index]
        self.can_switch_weapon = True
        self.weapon_switch_time = None
        self.switch_duration_cooldown = 200


        #stat
        self.stats = {"health": 100, "energy": 50, "attack": 10, "magic": 5, "speed": 5}
        self.health = self.stats["health"] * 0.5
        self.energy = self.stats["energy"] * 0.8
        self.xp = 666
        self.sp = self.stats["speed"]

    def import_player_asset (self):
        character_path = "./graphics/player/"
        self.animations = {"up": [], "down": [], "left": [], "right": [],
                           "right_idle": [], "left_idle": [], "up_idle": [], "down_idle": [],
                           "right_attack": [], "left_attack": [], "up_attack": [], "down_attack": []}
        
        for animation in self.animations.keys ():
            full_path = character_path + animation
            self.animations [animation] = import_folder (full_path)

    def input (self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.status = "up"
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1 
            self.status = "down"
        else:
            self.direction.y = 0
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.status = "right"
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.status = "left"
        else:
            self.direction.x = 0

        #attack
        if keys [pygame.K_SPACE] and not self.attacking:
            self.attacking = True
            self.attack_time = pygame.time.get_ticks ()
            self.create_attack () #problema de blit // não ataca mais de +1

        #magic
        if keys [pygame.K_LCTRL] and not self.attacking:
            self.attacking = True
            self.attack_time = pygame.time.get_ticks ()
            print ("magic")

        if keys [pygame.K_q] and self.can_switch_weapon:
            self.can_switch_weapon = False
            self.weapon_switch_time = pygame.time.get_ticks()

            if self.weapon_index < len(list(weapon_data.keys())) - 1: #resolvido.
                self.weapon_index += 1 # só tem 3 AARGGGHHHHH
            else:
                self.weapon_index = 0

            self.weapon = list(weapon_data.keys())[self.weapon_index]

    def get_status (self):
        
        #idle
        if self.direction.x ==  0 and self.direction.y == 0:
            if not "idle" in self.status and not "attack" in self.status:
                self.status = self.status + "_idle"

        if self.attacking:
            self.direction.x = 0
            self.direction.y = 0
            if not "attack" in self.status:
                if "idle" in self.status:
                    #overwrite idle
                    self.status = self.status.replace ("_idle", "_attack")
                else:
                    self.status = self.status + "_attack"
        else:
            if "attack" in self.status:
                self.status = self.status.replace ("_attack", "")

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

    def cooldown (self):
        current_time = pygame.time.get_ticks () # if só roda uma vez mas o get ticks faz rodar infinitamente

        if self.attacking:
            if current_time - self.attack_time >= self.attack_cooldown:
                self.attacking  = False
                self.destroy_attack()
        if not self.can_switch_weapon:
            if current_time - self.weapon_switch_time >= self.switch_duration_cooldown:
                self.can_switch_weapon = True

    def animate (self):
        animation = self.animations [self.status]

        #loop do frame index
        self.frame_index += self.animation_sp
        if self.frame_index >= len(animation):
            self.frame_index = 0

        # image
        self.image = animation [int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)


    def update (self):
        
        self.input()
        self.cooldown()
        self.get_status()
        self.animate ()
        self.move(self.sp)
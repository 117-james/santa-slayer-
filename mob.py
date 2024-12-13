import pygame
from setting import *
from entity import *
from support import *

class Mob (Entity):
    def __init__ (self, mob_name, pos, groups, obstacle_sprites): #feijoada de PUTAAAAA

        #setup
        super().__init__(groups)
        self.sprite_type = "mob"

        #graphics
        self.import_graphics(mob_name)
        self.status = "idle"
        self.image = self.animation [self.status][self.frame_index]

        # mov
        self.rect = self.image.get_rect (topleft = pos)
        self.hitbox = self.rect.inflate(0, -10)
        self.obstacle_sprites = obstacle_sprites

        #stats nessa buceta então já que não tem speed // biblioteca em atributos
        self.mob_name = mob_name
        mob_info = mob_data [self.mob_name]
        self.health  = mob_info ["health"]
        self.xp = mob_info["xp"]
        self.sp = mob_info ["speed"]
        self.attack_damage = mob_info ["damage"]
        self.resistance = mob_info ["resistance"]
        self.attack_radius = mob_info ["attack_radius"]
        self.notice_radius= mob_info ["notice_radius"]
        self.attack_type = mob_info ["attack_type"]

        #interaction
        self.can_attack = True
        self.attack_time = None
        self.attack_cooldown = 400


    def import_graphics (self, name):
        self.animation = {"idle":[], "move":[], "attack":[]}
        main_path = f"./graphics/mob/{name}/"
        for animation in self.animation.keys():
            self.animation[animation] = import_folder(main_path + animation)

    def get_player_distance_direction (self, player):

        #odeio vetor
        mob_vec = pygame.math.Vector2(self.rect.center)
        player_vec = pygame.math.Vector2 (player.rect.center)
        distance = (player_vec - mob_vec).magnitude()

        if distance > 0:
            direction = (player_vec - mob_vec).normalize()

        else:
            direction = pygame.math.Vector2()

        return (distance, direction)

    def get_status (self, player):
        distance = self.get_player_distance_direction(player)[0]

        if distance <= self.attack_radius and self.can_attack:
            if self.status != "attack":
                self.frame_index = 0

        elif distance <= self.notice_radius:
            self.status = "move"

        else:
            self.status = "idle"    

    def action(self, player):
        if self.status == "attack":
            self.attack_time = pygame.time.get_ticks()
        elif self.status == "move":
            self.direction = self.get_player_distance_direction(player)[1]
        else:
            self.direction = pygame.math.Vector2()

    def animate(self):
        animation = self.animation[self.status]
        
        self.frame_index += self.animation_sp
        if self.frame_index >= len(animation):

            if self.status == "attack":
                self.can_attack = False #o player só para de poder atacar depois da animação

            self.frame_index = 0

        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)

    def cooldown(self):
        if not self.can_attack:
            current_time = pygame.time.get_ticks()
            if current_time - self.attack_time >= self.attack_cooldown:
                self.can_attack = True

    def update(self):

        self.move(self.sp)
        self.animate()
        self.cooldown()

    def mob_update (self, player):
        self.get_status(player)
        self.action(player)
        
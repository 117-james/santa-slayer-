import pygame
WIDTH = 640
HEIGHT = 480
FPS = 60
TILESIZE = 32


weapon_data = {
    "sword": {"cooldown": 100, "damage": 15, "graphics": "./graphics/weapon/sword/full.png"},
    "axe": {"cooldown": 400, "damage": 30, "graphics": "./graphics/weapon/axe/full.png"},
    "lance": {"cooldown": 300, "damage": 20, "graphics": "./graphics/weapon/lance/full.png"}
}
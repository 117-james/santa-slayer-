import pygame
WIDTH = 640
HEIGHT = 480
FPS = 60
TILESIZE = 32

#ui
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = "./graphics/font/font.ttf"
UI_FONT_SIZE = 15

#general colours
WATER_COLOUR = "#70BDC9"
UI_BG_COLOUR = "#000000"
UI_BORDER_COLOUR = "#222222"
TEXT_COLOUR = "#E2D9D9"

# UI colours
HEALTH_COLOUR = "red"
ENERGY_COLOUR = "blue"
UI_BORDER_COLOUR_ACTIVE = "#C88A17"

weapon_data = {
    "sword": {"cooldown": 100, "damage": 15, "graphics": "./graphics/weapon/sword/full.png"},
    "axe": {"cooldown": 400, "damage": 30, "graphics": "./graphics/weapon/axe/full.png"},
    "lance": {"cooldown": 300, "damage": 20, "graphics": "./graphics/weapon/lance/full.png"}
}
import pygame
from setting import *

def display_dialogue(screen, dialogue_lines):
    font = pygame.font.Font(UI_FONT, 20)
    for line in dialogue_lines:
        screen.fill("black")
        text_surface = font.render(line, True, TEXT_COLOUR)
        text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text_surface, text_rect)
        pygame.display.update()
        pygame.time.wait(3000)  # each line is 3 seconds

import pygame
from setting import *
from dialogue import *

#variável global
dialogue_triggered = False

def final_battle(player, krampus, screen, clock, visible_sprites):
    global dialogue_triggered

    #pular diálogo
    if dialogue_triggered:
        return

    #clear events e pausa qualquer delay antes da transição
    pygame.event.clear()  
    clock.tick(0) 

    
    fade_to_black(screen, clock)

    #antes da batalha
    fight_dialogue = [
        "KRAMPUS: you dare challenge me on this blood moon..?",
        "KRAMPUS: look around, your holiday is ash!",
        "KRAMPUS: this isn't your fight anymore. it's mine to finish."
    ]
    display_dialogue(screen, fight_dialogue)  #display sequência

    # Step 3: Fade back to the game
    fade_from_black(screen, clock)

    #diálogo completo
    dialogue_triggered = True

    return

def fade_to_black(screen, clock, duration=1000):
    fade_surface = pygame.Surface((WIDTH, HEIGHT))
    fade_surface.fill((0, 0, 0))
    for alpha in range(0, 255, 5):
        fade_surface.set_alpha(alpha)
        screen.blit(fade_surface, (0, 0))
        pygame.display.update()
        clock.tick(FPS)

def fade_from_black(screen, clock, duration=1000):
    fade_surface = pygame.Surface((WIDTH, HEIGHT))
    fade_surface.fill((0, 0, 0))
    for alpha in range(255, 0, -5):
        fade_surface.set_alpha(alpha)
        screen.blit(fade_surface, (0, 0))
        pygame.display.update()
        clock.tick(FPS)

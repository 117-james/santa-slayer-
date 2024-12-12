import pygame
import sys
from setting import *
from level import *
from player import *

# playlist pra programar bem:
# i'm with you // avril lavigne
# amoeba // clairo
# drive // incubus
# peach // kevin abstract

class Game:
    def __init__ (self):
        # setup básico
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("SANTA SLAYER: BLOOD MOON")
        self.clock = pygame.time.Clock()
        self.level = Level()

    # Inicializar música para o menu
        pygame.mixer.music.load("./audio/Santa_Baby.mp3")  
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)  # Toca em loop infinito

        
    def run (self):

         # Parar música do menu e começar música de gameplay
        pygame.mixer.music.stop()
        pygame.mixer.music.load("./audio/Wicked Game.mp3") 
        pygame.mixer.music.play(-1) 

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill("grey")
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == "__main__":
    game = Game()
    game.run()

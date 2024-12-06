import pygame
import sys
from setting import *
from level import *


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
        

    def run (self):

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
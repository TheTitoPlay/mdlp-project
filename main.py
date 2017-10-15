#!/usr/bin/env python
#
# Game for MDLP Project
#
#git@github.com:TheTitoPlay/mdlp-project.git
#https://github.com/TheTitoPlay/mdlp-project.git

import pygame

class UntitledGame:

    def __init__(self):
        ## initialize screen
        pygame.init()
        ## window parameters
        self._window = pygame.display.set_mode((600, 420), pygame.DOUBLEBUF)
        pygame.display.set_caption('Awsome Untitled Platformer Game')
        pygame.display.set_icon(pygame.image.load('icon.png'))

        ## create screen
        self._screen = pygame.Surface(self._window.get_size(), pygame.SRCALPHA, 32)
        self._screen = self._screen.convert()
        self._bgcolor = (250, 250, 250)
        self._screen.fill(self._bgcolor)
        
        ## update screen
        self._window.blit(self._screen, (0, 0))
        pygame.display.flip()
        

    def run (self):
        done = False
        while done == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT :
                    done = True












        ## update screen
        self._window.blit(self._screen, (0, 0))
        pygame.display.flip()

        
        pygame.quit()


if __name__ == '__main__':
    game = UntitledGame()
    game.run()

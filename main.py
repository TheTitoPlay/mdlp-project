''' git@github.com:TheTitoPlay/mdlp-project.git |
    https://github.com/TheTitoPlay/mdlp-project.git'''

import pygame

class UntitledGame:

    def __init__(self):
        ## initialize pygame
        pygame.init()

        ## open new window
        window = pygame.display.set_mode((600, 420), pygame.DOUBLEBUF)
        pygame.display.set_caption('POP CULTURE VOL.1')
        pygame.display.set_icon(pygame.image.load('icon.png'))

        ## create canvas
        self._canvas = pygame.Surface((600, 420), pygame.SRCALPHA, 32)


        done = False
        while done == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT :
                    done = True














        pygame.quit()
    




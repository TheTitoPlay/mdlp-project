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
        self._window = pygame.display.set_mode((1000, 600), pygame.DOUBLEBUF)
        pygame.display.set_caption('Awsome Untitled Platformer Game')
        #pygame.display.set_icon(pygame.image.load('icon.png'))

        ## create screen
        self._screen = pygame.Surface(self._window.get_size(), pygame.SRCALPHA, 32)
        self._screen = self._screen.convert()
        #self._bgcolor = (0, 191, 255)
        #self._screen.fill(self._bgcolor)

        ## display/load menu
        self._menu = pygame.image.load('resources\screen\menu.png').convert()
        self._play = pygame.image.load('resources\screen\play.png').convert()
        self._screen.blit(self._menu, (0, 0))

        ## update screen        
        self._window.blit(self._screen, (0, 0))
        pygame.display.flip()

    def update_screen(self):
        ## update screen        
        self._window.blit(self._screen, (0, 0))
        pygame.display.flip()       
        

    def menu(self):        
        done = False
        menu_screen = 0
        while done == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT :
                    done = True                    

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 :
                        pos = event.pos
                        print(pos)

                        ## Play
                        if 408 < pos[0] < 587 and 250 < pos[1] < 319 and menu_screen == 0:
                            print("PLAY")
                            menu_screen = 1
                            self._screen.blit(self._play, (0, 0))
                            self.update_screen()
                        ## Play - New Game
                        if 383 < pos[0] < 616 and 254 < pos[1] < 308 and menu_screen == 1:
                            print("New Game")
                        ## Play - Continue Game
                        if 347 < pos[0] < 655 and 364 < pos[1] < 415 and menu_screen == 1:
                            print("Continue Game")
                        ## Play - Back to Menu
                        if 341 < pos[0] < 661 and 473 < pos[1] < 526 and menu_screen == 1:
                            menu_screen = 0
                            self._screen.blit(self._menu, (0, 0))
                            self.update_screen()
                            
                        ## Settings
                        if 349 < pos[0] < 648 and 359 < pos[1] < 428 and menu_screen == 0:
                            print("SETTINGS")
                            '''menu_screen = 2'''
                        ## Quit
                        if 425 < pos[0] < 573 and 542 < pos[1] < 591 and menu_screen == 0:
                            done = True


        ## update screen
        #self.update_screen()

        
        pygame.quit()


if __name__ == '__main__':
    game = UntitledGame()
    game.menu()

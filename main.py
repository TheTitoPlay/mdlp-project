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
        self._choose_player = pygame.image.load('resources\screen\choose_player.png').convert()
        self._player_pick = pygame.image.load('resources\screen\player_pick.png').convert_alpha()
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
                        if 416 < pos[0] < 584 and 225 < pos[1] < 286 and menu_screen == 0:
                            self._screen.blit(self._play, (0, 0))                            
                            self.update_screen()
                            menu_screen = 1
                        ## Play - New Game
                        if 390 < pos[0] < 613 and 297 < pos[1] < 354 and menu_screen == 1:
                            menu_screen = 12
                            self._screen.blit(self._choose_player, (0, 0))
                            p_position = 0
                            self._screen.blit(self._player_pick, (457, 337), (p_position,0,80,110))
                            self.update_screen()
                        ##Choose Previous Player                        
                        if 413 < pos[0] < 441 and 385 < pos[1] < 420 and menu_screen == 12 and p_position > 80:
                            self._screen.blit(self._choose_player, (0, 0))
                            p_position -= 81
                            self._screen.blit(self._player_pick, (457, 337), (p_position,0,80,110))
                            self.update_screen()
                        ##Choose Next Player
                        if 552 < pos[0] < 578 and 383 < pos[1] < 424 and menu_screen == 12 and p_position < 324:
                            self._screen.blit(self._choose_player, (0, 0))
                            p_position += 81
                            self._screen.blit(self._player_pick, (457, 337), (p_position,0,80,110))
                            self.update_screen()
                        ## Play - Continue Game
                        if 347 < pos[0] < 655 and 410 < pos[1] < 468 and menu_screen == 1:
                            print("Continue Game")
                        
                        ## Settings
                        if 359 < pos[0] < 646 and 376 < pos[1] < 432 and menu_screen == 0:
                            print("SETTINGS")
                            '''menu_screen = 2'''
                        ## Quit
                        if 425 < pos[0] < 573 and 542 < pos[1] < 591 and menu_screen == 0:
                            done = True
                ## Play - Return to Menu
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE :
                        menu_screen = 0
                        self._screen.blit(self._menu, (0, 0))
                        self.update_screen()

                    if event.key == pygame.K_RETURN and menu_screen == 12:
                        print("Jeu lancé avec perso choisi")
                        


        ## update screen
        #self.update_screen()

        
        pygame.quit()


if __name__ == '__main__':
    game = UntitledGame()
    game.menu()

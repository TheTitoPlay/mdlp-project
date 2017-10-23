#!/usr/bin/env python
#
# Game for MDLP Project
#
#git@github.com:TheTitoPlay/mdlp-project.git
#https://github.com/TheTitoPlay/mdlp-project.git

import pygame
from run import *
from player import *
from level_loader import *


class UntitledGame:

    def __init__(self):
        ## initialize screen
        pygame.init()

        ## window parameters
        self._window = pygame.display.set_mode((1024, 640), pygame.DOUBLEBUF)
        pygame.display.set_caption('Awsome Untitled Platformer Game')
        #pygame.display.set_icon(pygame.image.load('icon.png'))

        ## create screen
        self._screen = pygame.Surface(self._window.get_size(), pygame.SRCALPHA, 32)
        self._screen = self._screen.convert()
        self._bgcolor = (0, 191, 255)
        self._screen.fill(self._bgcolor)

        ## Initialize
        self._level_loader = LevelLoader()
        self._run = Run(self._screen.get_size())

        ## display/load menu
        self._menu = pygame.image.load('resources/screen/menu.png').convert_alpha()
        self._play = pygame.image.load('resources/screen/play.png').convert_alpha()
        self._choose_player = pygame.image.load('resources/screen/choose_player.png').convert_alpha()
        self._player_pick = pygame.image.load('resources/screen/player_pick.png').convert_alpha()
        self._screen.blit(self._menu, (0, 0))

        ## update screen        
        self._window.blit(self._screen, (0, 0))
        pygame.display.flip()

    def clear_menu(self):
        ## clear menu
        self._screen.fill(self._bgcolor)
        self.update_screen()
        
    def update_screen(self):
        ## update screen        
        self._window.blit(self._screen, (0, 0))
        pygame.display.flip()       
        

    def handler(self):        
        done = False
        menu_screen = 0
        while done == False:
            for event in pygame.event.get():
                ## Kill the Window when User kills it
                if event.type == pygame.QUIT:
                    done = True
                if menu_screen != -1:
                    ## Mouse Events Handling in MENU
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1 :
                            pos = event.pos

                            ## Play
                            if 428 < pos[0] < 596 and 225 < pos[1] < 286 and menu_screen == 0:
                                self.clear_menu()
                                self._screen.blit(self._play, (0, 0))                            
                                self.update_screen()
                                menu_screen = 1
                                
                            ## Play - New Game
                            if 402 < pos[0] < 625 and 297 < pos[1] < 354 and menu_screen == 1:
                                self.clear_menu()
                                menu_screen = 12
                                self._screen.blit(self._choose_player, (0, 0))
                                p_position = 0
                                self._screen.blit(self._player_pick, (470, 337), (p_position,0,80,110))
                                self.update_screen()
                                
                            ##Choose Previous Player                        
                            if 425 < pos[0] < 453 and 385 < pos[1] < 420 and menu_screen == 12 and p_position > 80:
                                self.clear_menu()
                                self._screen.blit(self._choose_player, (0, 0))
                                p_position -= 81
                                self._screen.blit(self._player_pick, (470, 337), (p_position,0,80,110))
                                self.update_screen()
                                
                            ##Choose Next Player
                            if 564 < pos[0] < 590 and 383 < pos[1] < 424 and menu_screen == 12 and p_position < 324:
                                self.clear_menu()
                                self._screen.blit(self._choose_player, (0, 0))
                                p_position += 81
                                self._screen.blit(self._player_pick, (470, 337), (p_position,0,80,110))
                                self.update_screen()
                                
                            ## Play - Continue Game
                            if 359 < pos[0] < 667 and 410 < pos[1] < 468 and menu_screen == 1:
                                print("Continue Game")
                            
                            ## Settings
                            if 371 < pos[0] < 658 and 376 < pos[1] < 432 and menu_screen == 0:
                                print("SETTINGS")
                                '''menu_screen = 2'''
                                
                            ## Quit
                            if 437 < pos[0] < 585 and 542 < pos[1] < 591 and menu_screen == 0:
                                done = True
                                
                    ## Keyboard Events Handling in MENU
                    if event.type == pygame.KEYDOWN:
                        
                        ##Return to Menu
                        if event.key == pygame.K_ESCAPE :
                            self.clear_menu()
                            menu_screen = 0
                            self._screen.blit(self._menu, (0, 0))
                            self.update_screen()

                        ## Choose Previous Player with Keyboard
                        if event.key == pygame.K_LEFT and menu_screen == 12 and p_position > 80:
                            self.clear_menu()
                            self._screen.blit(self._choose_player, (0, 0))
                            p_position -= 81
                            self._screen.blit(self._player_pick, (470, 337), (p_position,0,80,110))
                            self.update_screen()

                        ## Choose Next Player with Keyboard
                        if event.key == pygame.K_RIGHT and menu_screen == 12 and p_position < 324:
                            self.clear_menu()
                            self._screen.blit(self._choose_player, (0, 0))
                            p_position += 81
                            self._screen.blit(self._player_pick, (470, 337), (p_position,0,80,110))
                            self.update_screen()
                            
                        ## Set Selected Player
                        if event.key == pygame.K_RETURN and menu_screen == 12:
                            if p_position == 0:
                                player_selected = "adventurer"
                            if p_position == 81:
                                player_selected = "female"
                            if p_position == 162:
                                player_selected = "male"
                            if p_position == 243:
                                player_selected = "soldier"
                            if p_position == 324:
                                player_selected = "zombie"

                            ## Create New Game
                                
                            ##Initialize
                            self._player_right = PlayerSprites(player_selected, "right")
                            self._player_left = PlayerSprites(player_selected, "left")

                            ## Print New Game (Level 1 + Selected Player)
                            file = "resources/levels/1.lvl"
                            start_level = self._level_loader.load(file)

                            player = self._player_right.get_selected_player()
                            player_act = self._player_right.get_act("stand")
                            player_pos = 0, 0
                            
                            self._screen.blit(self._run.level(start_level, player, player_act, player_pos), (0, 0))
                            self.update_screen()
                            ## Switch to GAME mod
                            menu_screen = -1

                if menu_screen == -1:
                    ## Keyboard Events Handling in GAME
                    if event.type == pygame.KEYDOWN:

                        ## Return to Menu
                        if event.key == pygame.K_ESCAPE :
                            self.clear_menu()
                            menu_screen = 0
                            self._screen.blit(self._menu, (0, 0))
                            self.update_screen()
                            menu_screen = 0
                    
                        ## Move Right in Game
                        if event.key == pygame.K_RIGHT:
                            player = self._player_right.get_selected_player()
                            player_act = self._player_right.get_act("walk1")
                            player_pos = (player_pos[0] + 32, player_pos[1])
                            
                            self._screen.blit(self._run.level(start_level, player, player_act, player_pos), (0, 0))
                            self.update_screen()
                            
                        ## Move Left in Game
                        if event.key == pygame.K_LEFT:
                            player = self._player_left.get_selected_player()
                            player_act = self._player_left.get_act("walk1")
                            player_pos = (player_pos[0] - 32, player_pos[1])

                            self._screen.blit(self._run.level(start_level, player, player_act, player_pos), (0, 0))
                            self.update_screen()
                    
            ## Update screen
            self.update_screen()

        
        pygame.quit()


if __name__ == '__main__':
    launch = UntitledGame()
    launch.handler()

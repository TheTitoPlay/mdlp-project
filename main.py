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
from settings import *


class UntitledGame:

    def __init__(self):
        ## Initialize pygame and sound
        pygame.init()
        pygame.mixer.init()

        ## Window parameters
        self._window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.DOUBLEBUF)
        pygame.display.set_caption(TITLE)
        #pygame.display.set_icon(pygame.image.load('icon.png'))

        ## Create screen
        self._screen = pygame.Surface(self._window.get_size(), pygame.SRCALPHA, 32)
        self._screen = self._screen.convert()
        self._screen.fill(bgcolor)


        ## Initialize command to other files
        self._level_loader = LevelLoader()
        self._run = Run(self._screen.get_size())

        # Create Clock to watch FPS
        self._clock = pygame.time.Clock()

        # Repeate Pressed Keybord Events
        pygame.key.set_repeat(60, 0)

        ## Display/Load menu
        self._menu = pygame.image.load('resources/screen/menu.png').convert_alpha()
        self._play = pygame.image.load('resources/screen/play.png').convert_alpha()
        self._choose_player = pygame.image.load('resources/screen/choose_player.png').convert_alpha()
        self._player_pick = pygame.image.load('resources/screen/player_pick.png').convert_alpha()
        self._screen.blit(self._menu, (0, 0))

        ## Update screen
        self._window.blit(self._screen, (0, 0))
        pygame.display.flip()

    def clear_menu(self):
        ## Clear menu
        self._screen.fill(bgcolor)
        self.update_screen()

    def update_screen(self):
        ## Update screen
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

                            ## Choose Previous Player
                            if 425 < pos[0] < 453 and 385 < pos[1] < 420 and menu_screen == 12 and p_position > 80:
                                self.clear_menu()
                                self._screen.blit(self._choose_player, (0, 0))
                                p_position -= 81
                                self._screen.blit(self._player_pick, (470, 337), (p_position,0,80,110))
                                self.update_screen()

                            ## Choose Next Player
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
                                self._player_selected = "adventurer"
                            if p_position == 81:
                                self._player_selected = "female"
                            if p_position == 162:
                                self._player_selected = "male"
                            if p_position == 243:
                                self._player_selected = "soldier"
                            if p_position == 324:
                                self._player_selected = "zombie"

                            ## Create New Game

                            ##Initialize
                            self._dir = "right"
                            self._player_right = PlayerSprites(self._player_selected, "right")
                            self._player_left = PlayerSprites(self._player_selected, "left")

                            ## Print New Game (Level 1 + Selected Player)
                            self._start_file = "resources/levels/1.lvl"
                            self._start_level = self._level_loader.load(self._start_file)

                            self._player = self._player_right.get_selected_player()
                            self._player_act = self._player_right.get_act("stand")
                            self._player_pos = 0, 0

                            self._screen.blit(self._run.level(self._start_level, self._player, self._player_act, self._player_pos), (0, 0))
                            self.update_screen()
                            ## Switch to GAME mod
                            menu_screen = -1

                if menu_screen == -1:
                    ## Jump Handler
                    def jump(level, player, start_pos, direct):
                        self._player_direct = PlayerSprites(player, direct)
                        max_pos = start_pos[1] - 144
                        done = False
                        jump_status = 0
                        while done == False:

                            if jump_status == 0:
                                if start_pos[1] != max_pos:
                                    self._player = self._player_direct.get_selected_player()
                                    self._player_act = self._player_direct.get_act("jump")
                                    self._player_pos = (self._player_pos[0], self._player_pos[1] - 8)

                                    self._screen.blit(self._run.level(self._start_level, self._player, self._player_act, self._player_pos), (0, 0))
                                    self.update_screen()

                            if self._player_pos[1] == max_pos:
                                jump_status = 1

                            if jump_status == 1:
                                self._player = self._player_direct.get_selected_player()
                                self._player_act = self._player_direct.get_act("jump")
                                self._player_pos = (self._player_pos[0], self._player_pos[1] + 8)

                                self._screen.blit(self._run.level(self._start_level, self._player, self._player_act, self._player_pos), (0, 0))
                                self.update_screen()

                                if self._player_pos[1] == start_pos[1]:
                                    self._player_act = self._player_direct.get_act("stand")
                                    self._screen.blit(self._run.level(self._start_level, self._player, self._player_act, self._player_pos), (0, 0))
                                    self.update_screen()
                                    jump_status = 2
                                    done = True


                    ## Keyboard Down Events Handling in GAME
                    if event.type == pygame.KEYDOWN:

                        ## Return to Menu
                        if event.key == pygame.K_ESCAPE :
                            self.clear_menu()
                            menu_screen = 0
                            self._screen.blit(self._menu, (0, 0))
                            self.update_screen()
                            menu_screen = 0

                        ## Jump
                        elif event.key == pygame.K_SPACE:
                            jump(self._start_level, self._player_selected, self._player_pos, self._dir)


                        ## Move Right in Game
                        if event.key == pygame.K_RIGHT:
                            self._dir = "right"
                            self._player = self._player_right.get_selected_player()
                            self._player_act = self._player_right.get_act("walk")
                            self._player_pos = (self._player_pos[0] + 10, self._player_pos[1])

                            self._screen.blit(self._run.level(self._start_level, self._player, self._player_act, self._player_pos), (0, 0))
                            self.update_screen()

                        ## Move Left in Game
                        if event.key == pygame.K_LEFT:
                            self._dir = "left"
                            self._player = self._player_left.get_selected_player()
                            self._player_act = self._player_left.get_act("walk")
                            self._player_pos = (self._player_pos[0] - 10, self._player_pos[1])

                            self._screen.blit(self._run.level(self._start_level, self._player, self._player_act, self._player_pos), (0, 0))
                            self.update_screen()

                        ## Turn Back in Game
                        if event.key == pygame.K_UP:
                            self._player = self._player_right.get_selected_player()
                            self._player_act = self._player_right.get_act("back")

                            self._screen.blit(self._run.level(self._start_level, self._player, self._player_act, self._player_pos), (0, 0))
                            self.update_screen()

                        ## Test
                        if event.key == pygame.K_t:
                            self._player = self._player_right.get_selected_player()
                            self._player_act = self._player_right.get_act("swim")

                            self._screen.blit(self._run.level(self._start_level, self._player, self._player_act, self._player_pos), (0, 0))
                            self.update_screen()

                        ## Duck
                        if event.key == pygame.K_DOWN:
                            self._player = self._player_right.get_selected_player()
                            self._player_act = self._player_right.get_act("duck")
                            self._player_pos = (self._player_pos[0], self._player_pos[1] + 10)

                            self._screen.blit(self._run.level(self._start_level, self._player, self._player_act, self._player_pos), (0, 0))
                            self.update_screen()

                        '''## Jump 2Case
                        elif keys[pygame.K_SPACE]:
                            self._player = self._player_right.get_selected_player()
                            self._player_act = self._player_right.get_act("jump")
                            self._player_pos = (self._player_pos[0], self._player_pos[1] - 256)

                            self._screen.blit(self._run.level(self._start_level, self._player, self._player_act, self._player_pos), (0, 0))
                            self.update_screen()'''

                    ## Keyboard Up Events Handling in GAME
                    elif event.type == pygame.KEYUP:
                        if event.key == pygame.K_RIGHT:
                            self._player_act = self._player_right.get_act("stand")

                            self._screen.blit(self._run.level(self._start_level, self._player, self._player_act, self._player_pos), (0, 0))
                            self.update_screen()

                        elif event.key == pygame.K_LEFT:
                            self._player_act = self._player_left.get_act("stand")

                            self._screen.blit(self._run.level(self._start_level, self._player, self._player_act, self._player_pos), (0, 0))
                            self.update_screen()

                        elif event.key == pygame.K_UP:
                            self._player = self._player_right.get_selected_player()
                            self._player_act = self._player_right.get_act("stand")

                            self._screen.blit(self._run.level(self._start_level, self._player, self._player_act, self._player_pos), (0, 0))
                            self.update_screen()

                        if event.key == pygame.K_t:
                            self._player = self._player_right.get_selected_player()
                            self._player_act = self._player_right.get_act("stand")

                            self._screen.blit(self._run.level(self._start_level, self._player, self._player_act, self._player_pos), (0, 0))
                            self.update_screen()

                        ## Jump
                        #elif event.key == pygame.K_SPACE:
                            #jump(self._start_level, self._player_selected, self._player_pos, self._dir)

                        elif event.key == pygame.K_DOWN:
                            self._player = self._player_right.get_selected_player()
                            self._player_act = self._player_right.get_act("stand")

                            self._screen.blit(self._run.level(self._start_level, self._player, self._player_act, self._player_pos), (0, 0))
                            self.update_screen()


            ## Update screen
            self.update_screen()
            self._clock.tick(FPS)

        pygame.quit()


if __name__ == '__main__':
    launch = UntitledGame()
    launch.handler()

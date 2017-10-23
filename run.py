#!/usr/bin/env python
#
# Game for MDLP Project
#
#git@github.com:TheTitoPlay/mdlp-project.git
#https://github.com/TheTitoPlay/mdlp-project.git

import pygame




class Run:
    def __init__(self, screen_size):
        ## screen
        self._screen_size = screen_size
        
        ##Load Ressources
        self._bg = pygame.image.load('resources/game_sprites/PNG/Backgrounds/colored_land.png').convert()

        self._sprites = pygame.image.load('resources/game_sprites/Spritesheets/spritesheet_complete.png').convert_alpha()
        
        
    def level(self, level, player, player_act, player_pos):

        BS = 128
        run_surface = pygame.Surface(self._screen_size, pygame.SRCALPHA, 32)
        run_surface.blit(self._bg, (0,0), (0,300,1024,640))
        run_surface = run_surface.convert()

        Y_case = 0
        for line in level:
            X_case = 0
            for case in line:
                if case == "X":
                    run_surface.blit(self._sprites, (X_case, Y_case), (1690,390,BS,BS))
                if case == "G":
                    run_surface.blit(self._sprites, (X_case, Y_case), (1560,390,BS,BS))
                if case == "P":
                    run_surface.blit(player, (X_case + 24 + player_pos[0], Y_case + 18 + player_pos[1]), player_act)
                if case == "L":
                    run_surface.blit(self._sprites, (X_case, Y_case), (1560,1170,BS,BS))
                if case == "M":
                    run_surface.blit(self._sprites, (X_case, Y_case), (1560,1040,BS,BS))
                if case == "R":
                    run_surface.blit(self._sprites, (X_case, Y_case), (1560,910,BS,BS))

                X_case += BS
            Y_case += BS
        
        return run_surface 

        

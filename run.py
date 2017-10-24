#!/usr/bin/env python
#
# Game for MDLP Project
#
#git@github.com:TheTitoPlay/mdlp-project.git
#https://github.com/TheTitoPlay/mdlp-project.git

import pygame
from game_sprites import *




class Run:
    def __init__(self, screen_size):
        ## screen
        self._screen_size = screen_size
        
        ##Load Ressources
        self._bg = pygame.image.load('resources/game_sprites/PNG/Backgrounds/colored_land.png').convert()

        #self._sprites = pygame.image.load('resources/game_sprites/Spritesheets/spritesheet_complete.png').convert_alpha()
        self._game_sprites = GameSprites()
        self._get_sprites = self._game_sprites.get_sprites()
        
        
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
                    run_surface.blit(self._get_sprites, (X_case, Y_case), self._game_sprites.get_resources('grassCenter'))
                if case == "G":
                    run_surface.blit(self._get_sprites, (X_case, Y_case), self._game_sprites.get_resources('grassMid'))
                if case == "P":
                    run_surface.blit(player, (X_case + 24 + player_pos[0], Y_case + 18 + player_pos[1]), player_act)
                if case == "L":
                    run_surface.blit(self._get_sprites, (X_case, Y_case), self._game_sprites.get_resources('grassHalf_left'))
                if case == "M":
                    run_surface.blit(self._get_sprites, (X_case, Y_case), self._game_sprites.get_resources('grassHalf_mid'))
                if case == "R":
                    run_surface.blit(self._get_sprites, (X_case, Y_case), self._game_sprites.get_resources('grassHalf_right'))

                X_case += BS
            Y_case += BS
        
        return run_surface 

        

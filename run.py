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

        '''self._adventurer = pygame.image.load('resources/player/Adventurer/adventurer_tilesheet.png').convert_alpha()
        self._female = pygame.image.load('resources/player/Female/female_tilesheet.png').convert_alpha()
        self._male = pygame.image.load('resources/player/Player/player_tilesheet.png').convert_alpha()
        self._soldier = pygame.image.load('resources/player/Soldier/soldier_tilesheet.png').convert_alpha()
        self._zombie = pygame.image.load('resources/player/Zombie/zombie_tilesheet.png').convert_alpha()'''
        
        
    def game(self, level, player, start_pos):

        BS = 128
        game_surface = pygame.Surface(self._screen_size, pygame.SRCALPHA, 32)
        game_surface.blit(self._bg, (0,0), (0,300,1024,640))

        '''if player == "Adventurer":
            self._player_sprites = self._adventurer
        if player == "Female":
            self._player_sprites = self._female
        if player == "Male":
            self._player_sprites = self._male
        if player == "Soldier":
            self._player_sprites = self._soldier
        if player == "Zombie":
            self._player_sprites = self._zombie'''
        
        Y_case = 0
        for line in level:
            X_case = 0
            for case in line:
                if case == "X":
                    game_surface.blit(self._sprites, (X_case, Y_case), (1690,390,BS,BS))
                if case == "G":
                    game_surface.blit(self._sprites, (X_case, Y_case), (1560,390,BS,BS))
                if case == "P":
                    game_surface.blit(player, (X_case + 24, Y_case + 18), start_pos)
                if case == "L":
                    game_surface.blit(self._sprites, (X_case, Y_case), (1560,1170,BS,BS))
                if case == "M":
                    game_surface.blit(self._sprites, (X_case, Y_case), (1560,1040,BS,BS))
                if case == "R":
                    game_surface.blit(self._sprites, (X_case, Y_case), (1560,910,BS,BS))

                X_case += BS
            Y_case += BS
        
        return game_surface 

        

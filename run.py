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
        self._bg = pygame.image.load('resources/game_sprites/PNG/Backgrounds/colored_grass.png').convert()
        #self._player = player
        
    def make_bg(self):
        game_surface = pygame.Surface(self._screen_size, pygame.SRCALPHA, 32)
        game_surface.blit(self._bg, (0,0), (0,300,1000,600))
        #game_surface.blit(self._player, (0, 0))
        return game_surface 
        
        
    

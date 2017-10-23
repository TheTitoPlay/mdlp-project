#!/usr/bin/env python
#
# Game for MDLP Project
#
#git@github.com:TheTitoPlay/mdlp-project.git
#https://github.com/TheTitoPlay/mdlp-project.git

import pygame

class PlayerSprites:
    def __init__(self, player):
        ## Load corresponding resource
        self._selected_player = pygame.image.load("resources\player\\"  + player + "_tilesheet.png")



        ## Assign actions to their position
        self._action1 = pygame.Rect(320,110,80,110)
        self._action2 = pygame.Rect(400,110,80,110)
        self._back = pygame.Rect(320,220,80,110)
        self._cheer1 = pygame.Rect(560,0,80,110)
        self._cheer2 = pygame.Rect(640,0,80,110)
        self._climb1 = pygame.Rect(400,0,80,110) 
        self._climb2 = pygame.Rect(480,0,80,110) 
        self._duck = pygame.Rect(240,0,80,110)
        self._fall = pygame.Rect(160,0,80,110)
        self._hang = pygame.Rect(160,220,80,110)
        self._hold1 = pygame.Rect(160,110,80,110)
        self._hold2 = pygame.Rect(240,110,80,110)
        self._hurt = pygame.Rect(320,0,80,110)
        self._idle = pygame.Rect(0,0,80,110) 
        self._jump = pygame.Rect(80,0,80,110) 
        self._kick = pygame.Rect(480,110,80,110)
        self._skid = pygame.Rect(240,220,80,110)
        self._slide = pygame.Rect(80,220,80,110)
        self._stand = pygame.Rect(400,220,80,110)
        self._swim1 = pygame.Rect(560,110,80,110)
        self._swim2 = pygame.Rect(640,110,80,110) 
        self._talk = pygame.Rect(0,220,80,110)
        self._void = pygame.Rect(480,220,80,110)
        self._walk1 = pygame.Rect(0,110,80,110)
        self._walk2 = pygame.Rect(80,110,80,110)
                
    def get_selected_player(self):
        return self._selected_player

    def get_start_pos(self):
        return self._stand

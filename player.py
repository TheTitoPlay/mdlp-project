#!/usr/bin/env python
#
# Game for MDLP Project
#
#git@github.com:TheTitoPlay/mdlp-project.git
#https://github.com/TheTitoPlay/mdlp-project.git

import pygame

class PlayerSprites:
    def __init__(self, player, flip):
        ## Load corresponding resources
        if flip == 'right':
            self._selected_player = pygame.image.load("resources/player/"  + player + "_tilesheet.png")
        if flip == 'left':
            self._selected_player = pygame.image.load("resources/player/"  + player + "_tilesheet2.png")       
        
        ## Create Actions Lists
        self._walk = [pygame.Rect(80,110,80,110), pygame.Rect(0,110,80,110)]
        self._walks = 0
                
    def get_selected_player(self):
        ## Return Current Image
        return self._selected_player

    def get_act(self, act):
        ## Assign actions to their image location
        if act == 'action1':
            return pygame.Rect(320,110,80,110)
        if act == 'action2':
            return pygame.Rect(400,110,80,110)
        if act == 'back':
            return pygame.Rect(320,220,80,110)
        if act == 'cheer1':
            return pygame.Rect(560,0,80,110)
        if act == 'cheer2':
            return pygame.Rect(640,0,80,110)
        if act == 'climb1':
            return pygame.Rect(400,0,80,110) 
        if act == 'climb2':
            return pygame.Rect(480,0,80,110) 
        if act == 'duck':
            return pygame.Rect(240,0,80,110)
        if act == 'fall':
            return pygame.Rect(160,0,80,110)
        if act == 'hang':
            return pygame.Rect(160,220,80,110)
        if act == 'hold1':
            return pygame.Rect(160,110,80,110)
        if act == 'hold2':
            return pygame.Rect(240,110,80,110)
        if act == 'hurt':
            return pygame.Rect(320,0,80,110)
        if act == 'idle':
            return pygame.Rect(0,0,80,110) 
        if act == 'jump':
            return pygame.Rect(80,0,80,110)
        if act == 'kick':
            return pygame.Rect(480,110,80,110)
        if act == 'skid':
            return pygame.Rect(240,220,80,110)
        if act == 'slide':
            return pygame.Rect(80,220,80,110)
        if act == 'stand':
            return pygame.Rect(400,220,80,110)
        if act == 'swim1':
            return pygame.Rect(560,110,80,110)
        if act == 'swim2':
            return pygame.Rect(640,110,80,110) 
        if act == 'talk':
            return pygame.Rect(0,220,80,110)
        if act == 'void':
            return pygame.Rect(480,220,80,110)
        if act == 'walk1':
            return pygame.Rect(0,110,80,110)
        if act == 'walk2':
            return pygame.Rect(80,110,80,110)
        if act == 'walk':
            if self._walks == 1:
                self._walks = 0
                return self._walk[self._walks]
            
            if self._walks == 0:
                self._walks += 1
                return self._walk[self._walks]
            

#!/usr/bin/env python
#
# Game for MDLP Project
#
#git@github.com:TheTitoPlay/mdlp-project.git
#https://github.com/TheTitoPlay/mdlp-project.git

import pygame

class PlayerSprites:
    def __init__ (self, player):
        ## Load corresponding resource
        selected_player = pygame.image.load(str("resources\player\\"  + player + "_tilesheet.png"))
        ## Assign actions to their position
        action1 = pygame.Rect(320,110,80,110)
        action2 = pygame.Rect(400,110,80,110)
        back = pygame.Rect(320,220,80,110)
        cheer1 = pygame.Rect(560,0,80,110)
        cheer2 = pygame.Rect(640,0,80,110)
        climb1 = pygame.Rect(400,0,80,110) 
        climb2 = pygame.Rect(480,0,80,110) 
        duck = pygame.Rect(240,0,80,110)
        fall = pygame.Rect(160,0,80,110)
        hang = pygame.Rect(160,220,80,110)
        hold1 = pygame.Rect(160,110,80,110)
        hold2 = pygame.Rect(240,110,80,110)
        hurt = pygame.Rect(320,0,80,110)
        idle = pygame.Rect(0,0,80,110) 
        jump = pygame.Rect(80,0,80,110) 
        kick = pygame.Rect(480,110,80,110)
        skid = pygame.Rect(240,220,80,110)
        slide = pygame.Rect(80,220,80,110)
        stand = pygame.Rect(400,220,80,110)
        swim1 = pygame.Rect(560,110,80,110)
        swim2 = pygame.Rect(640,110,80,110) 
        talk = pygame.Rect(0,220,80,110)
        void = pygame.Rect(480,220,80,110)
        walk1 = pygame.Rect(0,110,80,110)
        walk2 = pygame.Rect(80,110,80,110)
        
        

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
        self._player_right = pygame.image.load("resources/player/"  + player + "_tilesheet.png").convert_alpha()
        self._player_left = pygame.image.load("resources/player/"  + player + "_tilesheet2.png").convert_alpha()

        if flip == 'right':
            self._selected_player = self._player_right
        if flip == 'left':
            self._selected_player = self._player_left

        ## Create Actions List
        self._action = [pygame.Rect(320,110,80,110), pygame.Rect(400,110,80,110)]
        self._actions = 0

        self._cheer = [pygame.Rect(560,0,80,110), pygame.Rect(640,0,80,110)]
        self._cheers = 0

        self._climb = [pygame.Rect(400,0,80,110), pygame.Rect(480,0,80,110)]
        self._climbs = 0

        self._stand = [pygame.Rect(0,0,80,110), pygame.Rect(400,220,80,110)]
        self._stands = 0

        self._swim = [pygame.Rect(560,110,80,110), pygame.Rect(640,110,80,110)]
        self._swims = 0

        self._walk = [pygame.Rect(80,110,80,110), pygame.Rect(0,110,80,110)]
        self._walks = 0

    def get_selected_player(self):
        ## Return Current Image
        return self._selected_player

    def get_act(self, act):
        ## Assign actions to their image location
        if act == 'action':
            if self._actions == 1:
                self._actions = 0
                return self._action[self._actions]

            if self._actions == 0:
                self._actions += 1
                return self._action[self._actions]

        if act == 'back':
            return pygame.Rect(320,220,80,110)

        if act == 'cheer':
            if self._cheers == 1:
                self._cheers = 0
                return self._cheer[self._cheers]

            if self._cheers == 0:
                self._cheers += 1
                return self._cheer[self._cheers]

        if act == 'climb':
            if self._climbs == 1:
                self._climbs = 0
                return self._climb[self._climbs]

            if self._climbs == 0:
                self._climbs += 1
                return self._climb[self._climbs]

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

        if act == 'jump':
            return pygame.Rect(80,0,80,110)

        if act == 'kick':
            return pygame.Rect(480,110,80,110)

        if act == 'skid':
            return pygame.Rect(240,220,80,110)

        if act == 'slide':
            return pygame.Rect(80,220,80,110)

        if act == 'stand':
            if self._stands == 1:
                self._stands = 0
                return self._stand[self._stands]

            if self._stands == 0:
                self._stands += 1
                return self._stand[self._stands]

        if act == 'swim':
            if self._swims == 1:
                self._swims = 0
                return self._swim[self._swims]

            if self._swims == 0:
                self._swims += 1
                return self._swim[self._swims]

        if act == 'talk':
            return pygame.Rect(0,220,80,110)

        if act == 'void':
            return pygame.Rect(480,220,80,110)

        if act == 'walk':
            if self._walks == 1:
                self._walks = 0
                return self._walk[self._walks]

            if self._walks == 0:
                self._walks += 1
                return self._walk[self._walks]

#!/usr/bin/env python
#
# Game for MDLP Project
#
#git@github.com:TheTitoPlay/mdlp-project.git
#https://github.com/TheTitoPlay/mdlp-project.git

import pygame
from settings import *
from game_sprites import *

class Level:
    def __init__(self, file):
        ## Read level given file and put it in a list
        F = open(file, 'r')
        self.level = []
        for line in F:
            self.level.append(list(line))
        F.close()

        if file == 'resources/levels/1.lvl':
            self.env_type = 'grass'

        if file == 'resources/levels/2.lvl':
            self.env_type = 'dirt'

        self.generate_level()

    def generate_level(self):

        self.level_env = {}

        Y_case = 0
        for line in self.level:
            X_case = 0
            for case in line:
                if case == "P":
                    self.player_start_pos = (X_case + 24, Y_case + 18)

                if case == "X":
                    self.env_maker(self.env_type + 'Center', X_case, Y_case)

                if case == "G":
                    self.env_maker(self.env_type + 'Mid', X_case, Y_case)

                if case == "L":
                    self.env_maker(self.env_type + 'Half_left', X_case, Y_case)

                if case == "M":
                    self.env_maker(self.env_type + 'Half_mid', X_case, Y_case)

                if case == "R":
                    self.env_maker(self.env_type + 'Half_right', X_case, Y_case)

                if case == "D":
                    self.env_maker('doorClosed_top', X_case, Y_case)

                if case == "k":
                    self.env_maker('keyYellow', X_case, Y_case)

                X_case += BS
            Y_case += BS

    def env_maker (self, sprite, X_case, Y_case):
        #Class all sprites in level_env
        try:
            self.level_env[sprite].append((X_case, Y_case, BS, BS))

        except:
            self.level_env[sprite] = [(X_case, Y_case, BS, BS)]


    def get_player_start_pos(self):
        return self.player_start_pos

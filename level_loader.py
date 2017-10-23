#!/usr/bin/env python
#
# Game for MDLP Project
#
#git@github.com:TheTitoPlay/mdlp-project.git
#https://github.com/TheTitoPlay/mdlp-project.git

class LevelLoader:
    def load(self, file):        
        ## Read level given file and put it in a list
        F = open(file, 'r')
        level = []
        for line in F:
            level.append(list(line))
        F.close()
        return level
        
        
        

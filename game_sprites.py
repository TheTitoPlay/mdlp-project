#!/usr/bin/env python
#
# Game for MDLP Project
#
#git@github.com:TheTitoPlay/mdlp-project.git
#https://github.com/TheTitoPlay/mdlp-project.git

import pygame
from settings import *

class GameSprites:
    '''def __init__(self):
        pass
        #self._game_sprites = pygame.image.load('resources/game_sprites/Spritesheets/spritesheet_complete.png').convert_alpha()'''

    def get_image_sprite(self, image, rect):
        image_s = pygame.Surface((rect[2], rect[3]), pygame.SRCALPHA, 32)
        image_s.blit(image, (0, 0), rect)
        return image_s

    def get_resources(self, resource):
        ## Assign resources to their image location
        ## Bomb
        if resource == 'bomb':
            return (2470, 520, 128, 128)
        if resource == 'bombWhite':
            return (2470, 390, 128, 128)

        ## Boxes
        if resource == 'boxCoin':
            return (2470, 260, 128, 128)
        if resource == 'boxCoin_boxed':
            return (2470, 130, 128, 128)
        if resource == 'boxCoin_disabled':
            return (2470, 0, 128, 128)
        if resource == 'boxCoin_disabled_boxed':
            return (2340, 1820, 128, 128)
        if resource == 'boxCrate':
            return (2340, 1690, 128, 128)
        if resource == 'boxCrate_double':
            return (2340, 1560, 128, 128)
        if resource == 'boxCrate_single':
            return (2340, 1430, 128, 128)
        if resource == 'boxCrate_warning':
            return (2340, 1300, 128, 128)
        if resource == 'boxExplosive':
            return (2340, 1170, 128, 128)
        if resource == 'boxExplosive_disabled':
            return (2340, 1040, 128, 128)
        if resource == 'boxExplosive_used':
            return (2340, 910, 128, 128)
        if resource == 'boxItem':
            return (2340, 780, 128, 128)
        if resource == 'boxItem_boxed':
            return (2340, 650, 128, 128)
        if resource == 'boxItem_disabled':
            return (2340, 520, 128, 128)
        if resource == 'boxItem_disabled_boxed':
            return (2340, 390, 128, 128)

        ## Bricks
        if resource == 'brickBrown':
            return (2340, 260, 128, 128)
        if resource == 'brickGrey':
            return (2340, 130, 128, 128)

        ## Bridges
        if resource == 'bridgeA':
            return (2340, 0, 128, 128)
        if resource == 'bridgeB':
            return (2210, 1820, 128, 128)

        ## Bushes
        if resource == 'bush':
            return (2210, 1690, 128, 128)
        if resource == 'cresourceus':
            return (2210, 1560, 128, 128)

        ## Chain
        if resource == 'chain':
            return (2210, 1430, 128, 128)

        ## Coins
        if resource == 'coinBronze':
            return (2730, 130, 128, 128)
        if resource == 'coinGold':
            return (2730, 0, 128, 128)
        if resource == 'coinSilver':
            return (2600, 1820, 128, 128)

        ## Dirt
        if resource == 'dirt':
            return (1820, 910, 128, 128)
        if resource == 'dirtCenter':
            return (1820, 780, 128, 128)
        if resource == 'dirtCenter_rounded':
            return (1820, 650, 128, 128)
        if resource == 'dirtCliffAlt_left':
            return (1820, 520, 128, 128)
        if resource == 'dirtCliffAlt_right':
            return (1820, 390, 128, 128)
        if resource == 'dirtCliff_left':
            return (1820, 260, 128, 128)
        if resource == 'dirtCliff_right':
            return (1820, 130, 128, 128)
        if resource == 'dirtCorner_left':
            return (1820, 0, 128, 128)
        if resource == 'dirtCorner_right':
            return (1690, 1820, 128, 128)
        if resource == 'dirtHalf':
            return (1690, 1690, 128, 74)
        if resource == 'dirtHalf_left':
            return (1690, 1560, 128, 74)
        if resource == 'dirtHalf_mid':
            return (1690, 1430, 128, 74)
        if resource == 'dirtHalf_right':
            return (1690, 1300, 128, 74)
        if resource == 'dirtHill_left':
            return (1690, 1170, 128, 128)
        if resource == 'dirtHill_right':
            return (1690, 1040, 128, 128)
        if resource == 'dirtLeft':
            return (1690, 910, 128, 128)
        if resource == 'dirtMid':
            return (1690, 780, 128, 128)
        if resource == 'dirtRight':
            return (1690, 650, 128, 128)

        ## Doors
        if resource == 'doorClosed_mid':
            return (2210, 1300, 128, 128)
        if resource == 'doorClosed_top':
            return (2210, 1170, 128, 256)
        if resource == 'doorOpen_mid':
            return (2210, 1040, 128, 128)
        if resource == 'doorOpen_top':
            return (2210, 910, 128, 256)

        ## Fences
        if resource == 'fence':
            return (2210,780, 128, 128)
        if resource == 'fenceBroken':
            return (2210, 650, 128, 128)

        ## Fireball
        if resource == 'fireball':
            return (2470, 650, 128, 128)

        ## Flags
        if resource == 'flagBlue1':
            return (2600, 1690, 128, 128)
        if resource == 'flagBlue2':
            return (2600, 1560, 128, 128)
        if resource == 'flagBlue_down':
            return (2600, 1430, 128, 128)
        if resource == 'flagGreen1':
            return (2600, 1300, 128, 128)
        if resource == 'flagGreen2':
            return (2600, 1170, 128, 128)
        if resource == 'flagGreen_down':
            return (2600, 1040, 128, 128)
        if resource == 'flagRed1':
            return (2600, 910, 128, 128)
        if resource == 'flagRed2':
            return (260, 780, 128, 128)
        if resource == 'flagRed_down':
            return (2600, 650, 128, 128)
        if resource == 'flagYellow1':
            return (2600, 520, 128, 128)
        if resource == 'flagYellow2':
            return (2600, 390, 128, 128)
        if resource == 'flagYellow_down':
            return (2600, 260, 128, 128)

        ## Gems
        if resource == 'gemBlue':
            return (2600, 130, 128, 128)
        if resource == 'gemGreen':
            return (2600, 0, 128, 128)
        if resource == 'gemRed':
            return (2470, 1820, 128, 128)
        if resource == 'gemYellow':
            return (2470, 1690, 128, 128)

        ## Grass
        if resource == 'grass':
            return (1690, 520, 128, 128)
        if resource == 'grassCenter':
            return (1690, 390, 128, 128)
        if resource == 'grassCenter_round':
            return (1690, 260, 128, 128)
        if resource == 'grassCliffAlt_left':
            return (1690, 130, 128, 128)
        if resource == 'grassCliffAlt_right':
            return (1690, 0, 128, 128)
        if resource == 'grassCliff_left':
            return (1560, 1820, 128, 128)
        if resource == 'grassCliff_right':
            return (1560, 1690, 128, 128)
        if resource == 'grassCorner_left':
            return (1560, 1560, 128, 128)
        if resource == 'grassCorner_right':
            return (1560, 1430, 128, 128)
        if resource == 'grassHalf':
            return (1560, 1300, 128, 74)
        if resource == 'grassHalf_left':
            return (1560, 1170, 128, 74)
        if resource == 'grassHalf_mid':
            return (1560, 1040, 128, 74)
        if resource == 'grassHalf_right':
            return (1560, 910, 128, 74)
        if resource == 'grassHill_left':
            return (1560, 780, 128, 128)
        if resource == 'grassHill_right':
            return (1560, 650, 128, 128)
        if resource == 'grassLeft':
            return (1560, 520, 128, 128)
        if resource == 'grassMid':
            return (1560, 390, 128, 128)
        if resource == 'grassRight':
            return (1560, 260, 128, 128)

        ## HUD
        if resource == 'hud0':
            return (2990, 910, 128, 128)
        if resource == 'hud1':
            return (2990, 650, 128, 128)
        if resource == 'hud2':
            return (2470, 910, 128, 128)
        if resource == 'hud3':
            return (2990, 520, 128, 128)
        if resource == 'hud4':
            return (2990, 390, 128, 128)
        if resource == 'hud5':
            return (2990, 260, 128, 128)
        if resource == 'hud6':
            return (2990, 130, 128, 128)
        if resource == 'hud7':
            return (2990, 0, 128, 128)
        if resource == 'hud8':
            return (2860, 1820, 128, 128)
        if resource == 'hud9':
            return (2860, 1690, 128, 128)

        if resource == 'hudCoin':
            return (2860, 1560, 128, 128)

        if resource == 'hudHeart_empty':
            return (2860, 1430, 128, 128)
        if resource == 'hudHeart_full':
            return (2860, 1300, 128, 128)
        if resource == 'hudHeart_half':
            return (2860,1170, 128, 128)

        if resource == 'hudJewel_blue':
            return (2860, 1040, 128, 128)
        if resource == 'hudJewel_blue_empty':
            return (2860, 910, 128, 128)
        if resource == 'hudJewel_green':
            return (2860, 780, 128, 128)
        if resource == 'hudJewel_green_empty':
            return (2860, 650, 128, 128)
        if resource == 'hudJewel_red':
            return (2860, 520, 128, 128)
        if resource == 'hudJewel_red_empty':
            return (2860, 390, 128, 128)
        if resource == 'hudJewel_yellow':
            return (2860, 260, 128, 128)
        if resource == 'hudJewel_yellow_empty':
            return (2860, 130, 128, 128)

        if resource == 'hudKey_blue':
            return (2860, 0, 128, 128)
        if resource == 'hudKey_blue_empty':
            return (2730, 1820, 128, 128)
        if resource == 'hudKey_green':
            return (2730, 1690, 128, 128)
        if resource == 'hudKey_green_empty':
            return (2730, 1560, 128, 128)
        if resource == 'hudKey_red':
            return (2730, 1430, 128, 128)
        if resource == 'hudKey_red_empty':
            return (2730, 1300, 128, 128)
        if resource == 'hudKey_yellow':
            return (2730, 1170, 128, 128)
        if resource == 'hudKey_yellow_empty':
            return (2730, 1040, 128, 128)

        if resource == 'hudX':
            return (2730, 260, 128, 128)


        ## Keys
        if resource == 'keyBlue':
            return (2470, 1560, 128, 128)
        if resource == 'keyGreen':
            return (2470, 1430, 128, 128)
        if resource == 'keyRed':
            return (2470, 1300, 128, 128)
        if resource == 'keyYellow':
            return (2470, 1170, 128, 128)


        ## Ladders
        if resource == 'ladderMid':
            return (2210, 390, 128, 128)
        if resource == 'ladderTop':
            return (2210, 260, 128, 128)


        ## Lava
        if resource == 'lava':
            return (2210, 130, 128, 128)
        if resource == 'lavaTop_high':
            return (2210, 0, 128, 128)
        if resource == 'lavaTop_low':
            return (2080, 1820, 128, 128)


        ## Levers
        if resource == 'leverLeft':
            return (2080, 1690, 128, 128)
        if resource == 'leverMid':
            return (2080, 1560, 128, 128)
        if resource == 'leverRight':
            return (2080, 1430, 128, 128)


        ## Locks
        if resource == 'lockBlue':
            return (2080, 1300, 128, 128)
        if resource == 'lockGreen':
            return (2080, 1170, 128, 128)
        if resource == 'lockRed':
            return (2080, 1040, 128, 128)
        if resource == 'lockYellow':
            return (2080, 910, 128, 128)


        ## Mushrooms
        if resource == 'mushroomBrown':
            return (2080, 780, 128, 128)
        if resource == 'mushroomRed':
            return (2080, 650, 128, 128)


        ## Planet
        if resource == 'planet':
            return (1560, 130, 128, 128)
        if resource == 'planetCenter':
            return (1560, 0, 128, 128)
        if resource == 'planetCenter_rounded':
            return (1430, 1820, 128, 128)
        if resource == 'planetCliffAlt_left':
            return (1430, 1690, 128, 128)
        if resource == 'planetCliffAlt_right':
            return (1430, 1560, 128, 128)
        if resource == 'planetCliff_left':
            return (1430, 1430, 128, 128)
        if resource == 'planetCliff_right':
            return (1430, 1300, 128, 128)
        if resource == 'planetCorner_left':
            return (1430, 1170, 128, 128)
        if resource == 'planetCorner_right':
            return (1430, 1040, 128, 128)
        if resource == 'planetHalf':
            return (1430, 910, 128, 74)
        if resource == 'planetHalf_left':
            return (1430, 780, 128, 74)
        if resource == 'planetHalf_mid':
            return (1430, 650, 128, 74)
        if resource == 'planetHalf_right':
            return (1430, 520, 128, 74)
        if resource == 'planetHill_left':
            return (1430, 390, 128, 128)
        if resource == 'planetHill_right':
            return (1430, 260, 128, 128)
        if resource == 'planetLeft':
            return (1430, 130, 128, 128)
        if resource == 'planetMid':
            return (1430, 0, 128, 128)
        if resource == 'planetRight':
            return (1300, 1820, 128, 128)


        ## Plant
        if resource == 'plantPurple':
            return (2080, 520, 128, 128)


        ## Rock
        if resource == 'rock':
            return (2080, 390, 128, 128)


        ## Sand
        if resource == 'sand':
            return (1300, 1690, 128, 128)
        if resource == 'sandCenter':
            return (1300, 1560, 128, 128)
        if resource == 'sandCenter_rounded':
            return (1300, 1430, 128, 128)
        if resource == 'sandCliffAlt_left':
            return (1300, 1300, 128, 128)
        if resource == 'sandCliffAlt_right':
            return (1300, 1170, 128, 128)
        if resource == 'sandCliff_left':
            return (1300, 1040, 128, 128)
        if resource == 'sandCliff_right':
            return (1300, 910, 128, 128)
        if resource == 'sandCorner_left':
            return (1300, 780, 128, 128)
        if resource == 'sandCorner_right':
            return (1300, 650, 128, 128)
        if resource == 'sandHalf':
            return (1300, 520, 128, 74)
        if resource == 'sandHalf_left':
            return (1300, 390, 128, 74)
        if resource == 'sandHalf_mid':
            return (1300, 260, 128, 74)
        if resource == 'sandHalf_right':
            return (1300, 130, 128, 74)
        if resource == 'sandHill_left':
            return (1300, 0, 128, 128)
        if resource == 'sandHill_right':
            return (1170, 1820, 128, 128)
        if resource == 'sandLeft':
            return (1170, 1690, 128, 128)
        if resource == 'sandMid':
            return (1170, 1560, 128, 128)
        if resource == 'sandRight':
            return (1170, 1430, 128, 128)


        ## Signs
        if resource == 'sign':
            return (2080, 260, 128, 128)
        if resource == 'signExit':
            return (2080, 130, 128, 128)
        if resource == 'signLeft':
            return (2080, 0, 128, 128)
        if resource == 'signRight':
            return (1950, 1820, 128, 128)


        ## Snow
        if resource == 'snow':
            return (1170, 1300, 128, 128)
        if resource == 'snowCenter':
            return (1170, 1170, 128, 128)
        if resource == 'snowCenter_rounded':
            return (1170, 1040, 128, 128)
        if resource == 'snowCliffAlt_left':
            return (1170, 910, 128, 128)
        if resource == 'snowCliffAlt_right':
            return (1170, 780, 128, 128)
        if resource == 'snowCliff_left':
            return (1170, 650, 128, 128)
        if resource == 'snowCliff_right':
            return (1170, 520, 128, 128)
        if resource == 'snowCorner_left':
            return (1170, 390, 128, 128)
        if resource == 'snowCorner_right':
            return (1170, 260, 128, 128)
        if resource == 'snowHalf':
            return (1170, 130, 128, 74)
        if resource == 'snowHalf_left':
            return (1170, 0, 128, 74)
        if resource == 'snowHalf_mid':
            return (1040, 1820, 128, 74)
        if resource == 'snowHalf_right':
            return (1040, 1690, 128, 74)
        if resource == 'snowHill_left':
            return (1040, 1560, 128, 128)
        if resource == 'snowHill_right':
            return (1040, 1430, 128, 128)
        if resource == 'snowLeft':
            return (1040, 1300, 128, 128)
        if resource == 'snowMid':
            return (1040, 1170, 128, 128)
        if resource == 'snowRight':
            return (1040, 1040, 128, 128)


        ## Spikes
        if resource == 'spikes':
            return (1950, 1560, 128, 128)


        ##Spring/Sprung
        if resource == 'spring':
            return (1950, 1430, 128, 128)
        if resource == 'sprung':
            return (1950, 1300, 128, 128)


        ## Star
        if resource == 'star':
            return (2470, 1040, 128, 128)


        ## Stone
        if resource == 'stone':
            return (1040, 910, 128, 128)
        if resource == 'stoneCenter':
            return (1040, 780, 128, 128)
        if resource == 'stoneCenter_rounded':
            return (1040, 650, 128, 128)
        if resource == 'stoneCliffAlt_left':
            return (1040, 520, 128, 128)
        if resource == 'stoneCliffAlt_right':
            return (1040, 390, 128, 128)
        if resource == 'stoneCliff_left':
            return (1040, 260, 128, 128)
        if resource == 'stoneCliff_right':
            return (1040, 130, 128, 128)
        if resource == 'stoneCorner_left':
            return (1040, 0, 128, 128)
        if resource == 'stoneCorner_right':
            return (910, 1808, 128, 128)
        if resource == 'stoneHalf':
            return (910, 678, 128, 74)
        if resource == 'stoneHalf_left':
            return (910, 1548, 128, 74)
        if resource == 'stoneHalf_mid':
            return (780, 1806, 128, 74)
        if resource == 'stoneHalf_right':
            return (650, 1806, 128, 74)
        if resource == 'stoneHill_left':
            return (520, 1806, 128, 128)
        if resource == 'stoneHill_right':
            return (390, 1806, 128, 128)
        if resource == 'stoneLeft':
            return (260, 1806, 128, 128)
        if resource == 'stoneMid':
            return (130, 1806, 128, 128)
        if resource == 'stoneRight':
            return (0, 1806, 128, 128)


        ## Switchs
        if resource == 'switchBlue':
            return (1950, 1170, 128, 128)
        if resource == 'switchBlue_pressed':
            return (1950, 1040, 128, 128)
        if resource == 'switchGreen':
            return (2470, 780, 128, 128)
        if resource == 'switchGreen_pressed':
            return (1950, 780, 128, 128)
        if resource == 'switchRed':
            return (1950, 650, 128, 128)
        if resource == 'switchRed_pressed':
            return (1950, 520, 128, 128)
        if resource == 'switchYellow':
            return (1950, 390, 128, 128)
        if resource == 'switchYellow_pressed':
            return (1950, 260, 128, 128)


        ## Torchs
        if resource == 'torch1':
            return (1950, 130, 128, 128)
        if resource == 'torch2':
            return (1950, 0, 128, 128)
        if resource == 'torchOff':
            return (1820, 1820, 128, 128)


        ## Water
        if resource == 'water':
            return (1820, 1690, 128, 128)
        if resource == 'waterTop_high':
            return (1820, 1560, 128, 128)
        if resource == 'waterTop_low':
            return (1820, 1430, 128, 128)


        ## Weights
        if resource == 'weight':
            return (1820, 1300, 128, 128)
        if resource == 'weightAttached':
            return (1820, 1170, 128, 128)


        ## Window
        if resource == 'window':
            return (1820, 1040, 128, 128)

#!/usr/bin/env python
#
# Game for MDLP Project
#
#git@github.com:TheTitoPlay/mdlp-project.git
#https://github.com/TheTitoPlay/mdlp-project.git

import pygame

class GameSprites:
    def __init__(self):
        self._game_sprites = pygame.image.load('resources/game_sprites/Spritesheets/spritesheet_complete.png').convert_alpha()

    def get_sprites(self):
        return self._game_sprites

    def get_resources(self, resource):
        ## Assign resources to their image location
        ## Bomb
        if resource == 'bomb':
            return pygame.Rect(2470, 520, 128, 128)
        if resource == 'bombWhite':
            return pygame.Rect(2470, 390, 128, 128)

        ## Boxes
        if resource == 'boxCoin':
            return pygame.Rect(2470, 260, 128, 128)
        if resource == 'boxCoin_boxed':
            return pygame.Rect(2470, 130, 128, 128)
        if resource == 'boxCoin_disabled':
            return pygame.Rect(2470, 0, 128, 128)
        if resource == 'boxCoin_disabled_boxed':
            return pygame.Rect(2340, 1820, 128, 128)
        if resource == 'boxCrate':
            return pygame.Rect(2340, 1690, 128, 128)
        if resource == 'boxCrate_double':
            return pygame.Rect(2340, 1560, 128, 128)
        if resource == 'boxCrate_single':
            return pygame.Rect(2340, 1430, 128, 128)
        if resource == 'boxCrate_warning':
            return pygame.Rect(2340, 1300, 128, 128)
        if resource == 'boxExplosive':
            return pygame.Rect(2340, 1170, 128, 128)
        if resource == 'boxExplosive_disabled':
            return pygame.Rect(2340, 1040, 128, 128)
        if resource == 'boxExplosive_used':
            return pygame.Rect(2340, 910, 128, 128)
        if resource == 'boxItem':
            return pygame.Rect(2340, 780, 128, 128)
        if resource == 'boxItem_boxed':
            return pygame.Rect(2340, 650, 128, 128)
        if resource == 'boxItem_disabled':
            return pygame.Rect(2340, 520, 128, 128)
        if resource == 'boxItem_disabled_boxed':
            return pygame.Rect(2340, 390, 128, 128)

        ## Bricks
        if resource == 'brickBrown':
            return pygame.Rect(2340, 260, 128, 128)
        if resource == 'brickGrey':
            return pygame.Rect(2340, 130, 128, 128)

        ## Bridges
        if resource == 'bridgeA':
            return pygame.Rect(2340, 0, 128, 128)
        if resource == 'bridgeB':
            return pygame.Rect(2210, 1820, 128, 128)
        
        ## Bushes
        if resource == 'bush':
            return pygame.Rect(2210, 1690, 128, 128)
        if resource == 'cresourceus':
            return pygame.Rect(2210, 1560, 128, 128)

        ## Chain
        if resource == 'chain':
            return pygame.Rect(2210, 1430, 128, 128)

        ## Coins
        if resource == 'coinBronze':
            return pygame.Rect(2730, 130, 128, 128)
        if resource == 'coinGold':
            return pygame.Rect(2730, 0, 128, 128)
        if resource == 'coinSilver':
            return pygame.Rect(2600, 1820, 128, 128)

        ## Dirt
        if resource == 'dirt':
            return pygame.Rect(1820, 910, 128, 128)
        if resource == 'dirtCenter':
            return pygame.Rect(1820, 780, 128, 128)
        if resource == 'dirtCenter_rounded':
            return pygame.Rect(1820, 650, 128, 128)
        if resource == 'dirtCliffAlt_left':
            return pygame.Rect(1820, 520, 128, 128)
        if resource == 'dirtCliffAlt_right':
            return pygame.Rect(1820, 390, 128, 128)
        if resource == 'dirtCliff_left':
            return pygame.Rect(1820, 260, 128, 128)
        if resource == 'dirtCliff_right':
            return pygame.Rect(1820, 130, 128, 128)
        if resource == 'dirtCorner_left':
            return pygame.Rect(1820, 0, 128, 128)
        if resource == 'dirtCorner_right':
            return pygame.Rect(1690, 1820, 128, 128)
        if resource == 'dirtHalf':
            return pygame.Rect(1690, 1690, 128, 128)
        if resource == 'dirtHalf_left':
            return pygame.Rect(1690, 1560, 128, 128)
        if resource == 'dirtHalf_mid':
            return pygame.Rect(1690, 1430, 128, 128)
        if resource == 'dirtHalf_right':
            return pygame.Rect(1690, 1300, 128, 128)
        if resource == 'dirtHill_left':
            return pygame.Rect(1690, 1170, 128, 128)
        if resource == 'dirtHill_right':
            return pygame.Rect(1690, 1040, 128, 128)
        if resource == 'dirtLeft':
            return pygame.Rect(1690, 910, 128, 128)
        if resource == 'dirtMid':
            return pygame.Rect(1690, 780, 128, 128)
        if resource == 'dirtRight':
            return pygame.Rect(1690, 650, 128, 128)

        ## Doors
        if resource == 'doorClosed_mid':
            return pygame.Rect(2210, 1300, 128, 128)
        if resource == 'doorClosed_top':
            return pygame.Rect(2210, 1170, 128, 128)
        if resource == 'doorOpen_mid':
            return pygame.Rect(2210, 1040, 128, 128)
        if resource == 'doorOpen_top':
            return pygame.Rect(2210, 910, 128, 128)

        ## Fences
        if resource == 'fence':
            return pygame.Rect(2210,780, 128, 128)
        if resource == 'fenceBroken':
            return pygame.Rect(2210, 650, 128, 128)

        ## Fireball
        if resource == 'fireball':
            return pygame.Rect(2470, 650, 128, 128)

        ## Flags
        if resource == 'flagBlue1':
            return pygame.Rect(2600, 1690, 128, 128)
        if resource == 'flagBlue2':
            return pygame.Rect(2600, 1560, 128, 128)
        if resource == 'flagBlue_down':
            return pygame.Rect(2600, 1430, 128, 128)
        if resource == 'flagGreen1':
            return pygame.Rect(2600, 1300, 128, 128)
        if resource == 'flagGreen2':
            return pygame.Rect(2600, 1170, 128, 128)
        if resource == 'flagGreen_down':
            return pygame.Rect(2600, 1040, 128, 128)
        if resource == 'flagRed1':
            return pygame.Rect(2600, 910, 128, 128)
        if resource == 'flagRed2':
            return pygame.Rect(260, 780, 128, 128)
        if resource == 'flagRed_down':
            return pygame.Rect(2600, 650, 128, 128)
        if resource == 'flagYellow1':
            return pygame.Rect(2600, 520, 128, 128)
        if resource == 'flagYellow2':
            return pygame.Rect(2600, 390, 128, 128)
        if resource == 'flagYellow_down':
            return pygame.Rect(2600, 260, 128, 128)

        ## Gems
        if resource == 'gemBlue':
            return pygame.Rect(2600, 130, 128, 128)
        if resource == 'gemGreen':
            return pygame.Rect(2600, 0, 128, 128)
        if resource == 'gemRed':
            return pygame.Rect(2470, 1820, 128, 128)
        if resource == 'gemYellow':
            return pygame.Rect(2470, 1690, 128, 128)

        ## Grass
        if resource == 'grass':
            return pygame.Rect(1690, 520, 128, 128)
        if resource == 'grassCenter':
            return pygame.Rect(1690, 390, 128, 128)
        if resource == 'grassCenter_round':
            return pygame.Rect(1690, 260, 128, 128)
        if resource == 'grassCliffAlt_left':
            return pygame.Rect(1690, 130, 128, 128)
        if resource == 'grassCliffAlt_right':
            return pygame.Rect(1690, 0, 128, 128)
        if resource == 'grassCliff_left':
            return pygame.Rect(1560, 1820, 128, 128)
        if resource == 'grassCliff_right':
            return pygame.Rect(1560, 1690, 128, 128)
        if resource == 'grassCorner_left':
            return pygame.Rect(1560, 1560, 128, 128)
        if resource == 'grassCorner_right':
            return pygame.Rect(1560, 1430, 128, 128)
        if resource == 'grassHalf':
            return pygame.Rect(1560, 1300, 128, 128)
        if resource == 'grassHalf_left':
            return pygame.Rect(1560, 1170, 128, 128)
        if resource == 'grassHalf_mid':
            return pygame.Rect(1560, 1040, 128, 128)
        if resource == 'grassHalf_right':
            return pygame.Rect(1560, 910, 128, 128)
        if resource == 'grassHill_left':
            return pygame.Rect(1560, 780, 128, 128)
        if resource == 'grassHill_right':
            return pygame.Rect(1560, 650, 128, 128)
        if resource == 'grassLeft':
            return pygame.Rect(1560, 520, 128, 128)
        if resource == 'grassMid':
            return pygame.Rect(1560, 390, 128, 128)
        if resource == 'grassRight':
            return pygame.Rect(1560, 260, 128, 128)

        ## HUD
        if resource == 'hud0':
            return pygame.Rect(2990, 910, 128, 128)
        if resource == 'hud1':
            return pygame.Rect(2990, 650, 128, 128)
        if resource == 'hud2':
            return pygame.Rect(2470, 910, 128, 128)
        if resource == 'hud3':
            return pygame.Rect(2990, 520, 128, 128)
        if resource == 'hud4':
            return pygame.Rect(2990, 390, 128, 128)
        if resource == 'hud5':
            return pygame.Rect(2990, 260, 128, 128)
        if resource == 'hud6':
            return pygame.Rect(2990, 130, 128, 128)
        if resource == 'hud7':
            return pygame.Rect(2990, 0, 128, 128)
        if resource == 'hud8':
            return pygame.Rect(2860, 1820, 128, 128)
        if resource == 'hud9':
            return pygame.Rect(2860, 1690, 128, 128)        
        
        if resource == 'hudCoin':
            return pygame.Rect(2860, 1560, 128, 128)
        
        if resource == 'hudHeart_empty':
            return pygame.Rect(2860, 1430, 128, 128)
        if resource == 'hudHeart_full':
            return pygame.Rect(2860, 1300, 128, 128)
        if resource == 'hudHeart_half':
            return pygame.Rect(2860,1170, 128, 128)
        
        if resource == 'hudJewel_blue':
            return pygame.Rect(2860, 1040, 128, 128)
        if resource == 'hudJewel_blue_empty':
            return pygame.Rect(2860, 910, 128, 128)
        if resource == 'hudJewel_green':
            return pygame.Rect(2860, 780, 128, 128)
        if resource == 'hudJewel_green_empty':
            return pygame.Rect(2860, 650, 128, 128)
        if resource == 'hudJewel_red':
            return pygame.Rect(2860, 520, 128, 128)
        if resource == 'hudJewel_red_empty':
            return pygame.Rect(2860, 390, 128, 128)
        if resource == 'hudJewel_yellow':
            return pygame.Rect(2860, 260, 128, 128)
        if resource == 'hudJewel_yellow_empty':
            return pygame.Rect(2860, 130, 128, 128)
        
        if resource == 'hudKey_blue':
            return pygame.Rect(2860, 0, 128, 128)
        if resource == 'hudKey_blue_empty':
            return pygame.Rect(2730, 1820, 128, 128)
        if resource == 'hudKey_green':
            return pygame.Rect(2730, 1690, 128, 128)
        if resource == 'hudKey_green_empty':
            return pygame.Rect(2730, 1560, 128, 128)
        if resource == 'hudKey_red':
            return pygame.Rect(2730, 1430, 128, 128)
        if resource == 'hudKey_red_empty':
            return pygame.Rect(2730, 1300, 128, 128)
        if resource == 'hudKey_yellow':
            return pygame.Rect(2730, 1170, 128, 128)
        if resource == 'hudKey_yellow_empty':
            return pygame.Rect(2730, 1040, 128, 128)
        
        if resource == 'hudX':
            return pygame.Rect(2730, 260, 128, 128)


        ## Keys
        if resource == 'keyBlue':
            return pygame.Rect(2470, 1560, 128, 128)
        if resource == 'keyGreen':
            return pygame.Rect(2470, 1430, 128, 128)
        if resource == 'keyRed':
            return pygame.Rect(2470, 1300, 128, 128)
        if resource == 'keyYellow':
            return pygame.Rect(2470, 1170, 128, 128)


        ## Ladders
        if resource == 'ladderMid':
            return pygame.Rect(2210, 390, 128, 128)
        if resource == 'ladderTop':
            return pygame.Rect(2210, 260, 128, 128)


        ## Lava
        if resource == 'lava':
            return pygame.Rect(2210, 130, 128, 128)
        if resource == 'lavaTop_high':
            return pygame.Rect(2210, 0, 128, 128)
        if resource == 'lavaTop_low':
            return pygame.Rect(2080, 1820, 128, 128)


        ## Levers
        if resource == 'leverLeft':
            return pygame.Rect(2080, 1690, 128, 128)
        if resource == 'leverMid':
            return pygame.Rect(2080, 1560, 128, 128)
        if resource == 'leverRight':
            return pygame.Rect(2080, 1430, 128, 128)


        ## Locks
        if resource == 'lockBlue':
            return pygame.Rect(2080, 1300, 128, 128)
        if resource == 'lockGreen':
            return pygame.Rect(2080, 1170, 128, 128)
        if resource == 'lockRed':
            return pygame.Rect(2080, 1040, 128, 128)
        if resource == 'lockYellow':
            return pygame.Rect(2080, 910, 128, 128)


        ## Mushrooms
        if resource == 'mushroomBrown':
            return pygame.Rect(2080, 780, 128, 128)
        if resource == 'mushroomRed':
            return pygame.Rect(2080, 650, 128, 128)
        

        ## Planet
        if resource == 'planet':
            return pygame.Rect(1560, 130, 128, 128)
        if resource == 'planetCenter':
            return pygame.Rect(1560, 0, 128, 128)
        if resource == 'planetCenter_rounded':
            return pygame.Rect(1430, 1820, 128, 128)
        if resource == 'planetCliffAlt_left':
            return pygame.Rect(1430, 1690, 128, 128)
        if resource == 'planetCliffAlt_right':
            return pygame.Rect(1430, 1560, 128, 128)
        if resource == 'planetCliff_left':
            return pygame.Rect(1430, 1430, 128, 128)
        if resource == 'planetCliff_right':
            return pygame.Rect(1430, 1300, 128, 128)
        if resource == 'planetCorner_left':
            return pygame.Rect(1430, 1170, 128, 128)
        if resource == 'planetCorner_right':
            return pygame.Rect(1430, 1040, 128, 128)
        if resource == 'planetHalf':
            return pygame.Rect(1430, 910, 128, 128)
        if resource == 'planetHalf_left':
            return pygame.Rect(1430, 780, 128, 128)
        if resource == 'planetHalf_mid':
            return pygame.Rect(1430, 650, 128, 128)
        if resource == 'planetHalf_right':
            return pygame.Rect(1430, 520, 128, 128)
        if resource == 'planetHill_left':
            return pygame.Rect(1430, 390, 128, 128)
        if resource == 'planetHill_right':
            return pygame.Rect(1430, 260, 128, 128)
        if resource == 'planetLeft':
            return pygame.Rect(1430, 130, 128, 128)
        if resource == 'planetMid':
            return pygame.Rect(1430, 0, 128, 128)
        if resource == 'planetRight':
            return pygame.Rect(1300, 1820, 128, 128)


        ## Plant
        if resource == 'plantPurple':
            return pygame.Rect(2080, 520, 128, 128)


        ## Rock
        if resource == 'rock':
            return pygame.Rect(2080, 390, 128, 128)


        ## Sand
        if resource == 'sand':
            return pygame.Rect(1300, 1690, 128, 128)
        if resource == 'sandCenter':
            return pygame.Rect(1300, 1560, 128, 128)
        if resource == 'sandCenter_rounded':
            return pygame.Rect(1300, 1430, 128, 128)
        if resource == 'sandCliffAlt_left':
            return pygame.Rect(1300, 1300, 128, 128)
        if resource == 'sandCliffAlt_right':
            return pygame.Rect(1300, 1170, 128, 128)
        if resource == 'sandCliff_left':
            return pygame.Rect(1300, 1040, 128, 128)
        if resource == 'sandCliff_right':
            return pygame.Rect(1300, 910, 128, 128)
        if resource == 'sandCorner_left':
            return pygame.Rect(1300, 780, 128, 128)
        if resource == 'sandCorner_right':
            return pygame.Rect(1300, 650, 128, 128)
        if resource == 'sandHalf':
            return pygame.Rect(1300, 520, 128, 128)
        if resource == 'sandHalf_left':
            return pygame.Rect(1300, 390, 128, 128)
        if resource == 'sandHalf_mid':
            return pygame.Rect(1300, 260, 128, 128)
        if resource == 'sandHalf_right':
            return pygame.Rect(1300, 130, 128, 128)
        if resource == 'sandHill_left':
            return pygame.Rect(1300, 0, 128, 128)
        if resource == 'sandHill_right':
            return pygame.Rect(1170, 1820, 128, 128)
        if resource == 'sandLeft':
            return pygame.Rect(1170, 1690, 128, 128)
        if resource == 'sandMid':
            return pygame.Rect(1170, 1560, 128, 128)
        if resource == 'sandRight':
            return pygame.Rect(1170, 1430, 128, 128)


        ## Signs
        if resource == 'sign':
            return pygame.Rect(2080, 260, 128, 128)
        if resource == 'signExit':
            return pygame.Rect(2080, 130, 128, 128)
        if resource == 'signLeft':
            return pygame.Rect(2080, 0, 128, 128)
        if resource == 'signRight':
            return pygame.Rect(1950, 1820, 128, 128)


        ## Snow
        if resource == 'snow':
            return pygame.Rect(1170, 1300, 128, 128)
        if resource == 'snowCenter':
            return pygame.Rect(1170, 1170, 128, 128)
        if resource == 'snowCenter_rounded':
            return pygame.Rect(1170, 1040, 128, 128)
        if resource == 'snowCliffAlt_left':
            return pygame.Rect(1170, 910, 128, 128)
        if resource == 'snowCliffAlt_right':
            return pygame.Rect(1170, 780, 128, 128)
        if resource == 'snowCliff_left':
            return pygame.Rect(1170, 650, 128, 128)
        if resource == 'snowCliff_right':
            return pygame.Rect(1170, 520, 128, 128)
        if resource == 'snowCorner_left':
            return pygame.Rect(1170, 390, 128, 128)
        if resource == 'snowCorner_right':
            return pygame.Rect(1170, 260, 128, 128)
        if resource == 'snowHalf':
            return pygame.Rect(1170, 130, 128, 128)
        if resource == 'snowHalf_left':
            return pygame.Rect(1170, 0, 128, 128)
        if resource == 'snowHalf_mid':
            return pygame.Rect(1040, 1820, 128, 128)
        if resource == 'snowHalf_right':
            return pygame.Rect(1040, 1690, 128, 128)
        if resource == 'snowHill_left':
            return pygame.Rect(1040, 1560, 128, 128)
        if resource == 'snowHill_right':
            return pygame.Rect(1040, 1430, 128, 128)
        if resource == 'snowLeft':
            return pygame.Rect(1040, 1300, 128, 128)
        if resource == 'snowMid':
            return pygame.Rect(1040, 1170, 128, 128)
        if resource == 'snowRight':
            return pygame.Rect(1040, 1040, 128, 128)


        ## Spikes
        if resource == 'spikes':
            return pygame.Rect(1950, 1560, 128, 128)


        ##Spring/Sprung
        if resource == 'spring':
            return pygame.Rect(1950, 1430, 128, 128)
        if resource == 'sprung':
            return pygame.Rect(1950, 1300, 128, 128)


        ## Star
        if resource == 'star':
            return pygame.Rect(2470, 1040, 128, 128)


        ## Stone
        if resource == 'stone':
            return pygame.Rect(1040, 910, 128, 128)
        if resource == 'stoneCenter':
            return pygame.Rect(1040, 780, 128, 128)
        if resource == 'stoneCenter_rounded':
            return pygame.Rect(1040, 650, 128, 128)
        if resource == 'stoneCliffAlt_left':
            return pygame.Rect(1040, 520, 128, 128)
        if resource == 'stoneCliffAlt_right':
            return pygame.Rect(1040, 390, 128, 128)
        if resource == 'stoneCliff_left':
            return pygame.Rect(1040, 260, 128, 128)
        if resource == 'stoneCliff_right':
            return pygame.Rect(1040, 130, 128, 128)
        if resource == 'stoneCorner_left':
            return pygame.Rect(1040, 0, 128, 128)
        if resource == 'stoneCorner_right':
            return pygame.Rect(910, 1808, 128, 128)
        if resource == 'stoneHalf':
            return pygame.Rect(910, 678, 128, 128)
        if resource == 'stoneHalf_left':
            return pygame.Rect(910, 1548, 128, 128)
        if resource == 'stoneHalf_mid':
            return pygame.Rect(780, 1806, 128, 128)
        if resource == 'stoneHalf_right':
            return pygame.Rect(650, 1806, 128, 128)
        if resource == 'stoneHill_left':
            return pygame.Rect(520, 1806, 128, 128)
        if resource == 'stoneHill_right':
            return pygame.Rect(390, 1806, 128, 128)
        if resource == 'stoneLeft':
            return pygame.Rect(260, 1806, 128, 128)
        if resource == 'stoneMid':
            return pygame.Rect(130, 1806, 128, 128)
        if resource == 'stoneRight':
            return pygame.Rect(0, 1806, 128, 128)


        ## Switchs
        if resource == 'switchBlue':
            return pygame.Rect(1950, 1170, 128, 128)
        if resource == 'switchBlue_pressed':
            return pygame.Rect(1950, 1040, 128, 128)
        if resource == 'switchGreen':
            return pygame.Rect(2470, 780, 128, 128)
        if resource == 'switchGreen_pressed':
            return pygame.Rect(1950, 780, 128, 128)
        if resource == 'switchRed':
            return pygame.Rect(1950, 650, 128, 128)
        if resource == 'switchRed_pressed':
            return pygame.Rect(1950, 520, 128, 128)
        if resource == 'switchYellow':
            return pygame.Rect(1950, 390, 128, 128)
        if resource == 'switchYellow_pressed':
            return pygame.Rect(1950, 260, 128, 128)


        ## Torchs
        if resource == 'torch1':
            return pygame.Rect(1950, 130, 128, 128)
        if resource == 'torch2':
            return pygame.Rect(1950, 0, 128, 128)
        if resource == 'torchOff':
            return pygame.Rect(1820, 1820, 128, 128)


        ## Water
        if resource == 'water':
            return pygame.Rect(1820, 1690, 128, 128)
        if resource == 'waterTop_high':
            return pygame.Rect(1820, 1560, 128, 128)
        if resource == 'waterTop_low':
            return pygame.Rect(1820, 1430, 128, 128)


        ## Weights
        if resource == 'weight':
            return pygame.Rect(1820, 1300, 128, 128)
        if resource == 'weightAttached':
            return pygame.Rect(1820, 1170, 128, 128)


        ## Window
        if resource == 'window':
            return pygame.Rect(1820, 1040, 128, 128)
        

#!/usr/bin/env python
#
# Game for MDLP Project
#
#git@github.com:TheTitoPlay/mdlp-project.git
#https://github.com/TheTitoPlay/mdlp-project.git

import pygame
import os
from player import *
from level import *
from settings import *
from sprites import *

class UntitledGame:

    def __init__(self):
        # initialize game window, etc
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.load_resources()

    def load_resources(self):
        #menu
        self.menu = pygame.image.load('resources/screen/menu.png').convert_alpha()
        self.play = pygame.image.load('resources/screen/play.png').convert_alpha()
        self.new_game = pygame.image.load('resources/screen/choose_player.png').convert_alpha()
        self.player_pick = pygame.image.load('resources/screen/player_pick.png').convert_alpha()
        self.continue_game = pygame.image.load('resources/screen/continue_game.png').convert_alpha()
        #Game sprites
        self.game_sprites = pygame.image.load('resources/game_sprites/Spritesheets/spritesheet_complete.png').convert_alpha()
        self.data_player = 0

    def create_new_game(self):

        self.save_name = str(input("Username (without > < / \ * \" ' : ? |): "))

        try:
            with open("resources/saves/" + self.save_name + ".svg", 'x') as f:
                #        line 1                                     line 2
                f.write("player" + '\n' + str(self.data_player) + '\nlevel\n1')
                self.tilesheet = PlayerSprites('resources/player/' + P_PICK[int(self.data_player)] + '_tilesheet.png')
                self.level2load = "resources/levels/1.lvl"
                self.level_loaded = "1"
                self.saved_name = self.save_name

        except:
            print("Username already exists \(°O°*)/")
            self.save_not_exist = str(input("Do you want to choose another: y/n "))

            if self.save_not_exist == 'y':
                self.create_new_game()

            if self.save_not_exist == 'n':
                self.menu_display('play')
                self.waiting = False

    def load_game(self):
        self.saved_name = str(input("Username: "))
        try:
            with open("resources/saves/" + self.saved_name + ".svg", 'r') as f:
                self.save_list = []
                for line in f:
                    self.save_list.append(line)

                i = 0
                for element in self.save_list:
                    i +=1
                    if element == 'player\n':
                        self.data_player = self.save_list[i]

                    if element == 'level\n':
                        self.level_loaded = self.save_list[i]
                        self.level2load = 'resources/levels/' + self.save_list[i] + '.lvl'
            self.tilesheet = PlayerSprites('resources/player/' + P_PICK[int(self.data_player)] + '_tilesheet.png')

        except:
            print("Wrong username!")
            self.save_not_exist = str(input("Do you want to try again: y/n "))

            if self.save_not_exist == 'y':
                self.load_game()

            if self.save_not_exist == 'n':
                self.menu_display('play')
                self.waiting = False

            else:
                print("Error!")
                self.load_game()

    def save_game(self):
        self.level_loaded = str(int(self.level_loaded) + 1)
        with open("resources/saves/" + self.saved_name + ".svg", 'w') as f:
            #        line 1                                     line 2
            f.write("player" + '\n' + str(self.data_player) + 'level\n' + self.level_loaded)
            self.level2load = 'resources/levels/' + self.level_loaded + '.lvl'

    def game(self):
        # start the game
        # load & build level
        level = Level(self.level2load)
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.objects = pygame.sprite.Group()
        self.keys = pygame.sprite.Group()
        self.player = Player(self, P_PICK[int(self.data_player)], level.get_player_start_pos())
        self.all_sprites.add(self.player)

        #Hud
        self.hud_head = pygame.image.load('resources/player/'+ P_PICK[int(self.data_player)] + '/Limbs/head.png')

        #Game Init Vars
        self.door_open = False
        self.haveAkey = False
        self.num_key = 0
        self.key_hud = pygame.Surface((128, 128), pygame.SRCALPHA, 32)

        #Level sprites
        for keys in level.level_env.keys():
            for sprite in level.level_env[keys]:
                if 'sign' in keys:
                    s = Sprite(self.game_sprites, keys, sprite)
                    self.all_sprites.add(s)
                elif 'door' in keys:
                    self.door = DynamicSprite(self.game_sprites, keys, sprite)
                    self.all_sprites.add(self.door)
                elif 'key' in keys:
                    self.num_key += 1
                    k = Sprite(self.game_sprites, keys, sprite)
                    key = Key(self.game_sprites)
                    self.key_hud_empty = key.key_yellow
                    self.keys.add(k)
                    self.all_sprites.add(k)
                else:
                    p = Sprite(self.game_sprites, keys, sprite)
                    self.platforms.add(p)
                    self.all_sprites.add(p)

        print("Level " + self.level_loaded + " loaded!")
        print("May the force be with you " + self.saved_name + "!")
        self.handler()

    def handler(self):
        # Game Loopload_res
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # Game Loop - Update
        self.all_sprites.update()
        # player hits platforms when falling
        if self.player.vel.y > 0:
            hits = pygame.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                if self.player.pos.y < hits[0].rect.bottom:
                    self.player.pos.y = hits[0].rect.top + 1
                    self.player.vel.y = 0
                    self.player.jumping = False

        #player hits platforms when jumping
        if self.player.vel.y < 0:
            hits = pygame.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.bottom + 110
                self.player.vel.y = -(self.player.vel.y)

        # top scroll
        if self.player.rect.top <= HEIGHT / 6:
            self.player.pos.y += max(abs(self.player.vel.y), 5)
            for plat in self.all_sprites:
                plat.rect.y += max(abs(self.player.vel.y), 5)

        # down scroll
        if self.player.rect.bottom >= HEIGHT * (6 / 7):
            self.player.pos.y -= max(abs(self.player.vel.y), 5)
            for plat in self.all_sprites:
                plat.rect.y -= max(abs(self.player.vel.y), 5)

        # right scroll
        if self.player.rect.right >= WIDTH * (5/8):
            self.player.pos.x -= max(abs(self.player.vel.x), 5)
            for plat in self.all_sprites:
                plat.rect.x -= max(abs(self.player.vel.x), 5)

        # left scroll
        if self.player.rect.left <= WIDTH * (3/8):
            self.player.pos.x += max(abs(self.player.vel.x), 5)
            for plat in self.all_sprites:
                plat.rect.x += max(abs(self.player.vel.x), 5)

        # player grab key
        hits = pygame.sprite.spritecollide(self.player, self.keys, True)
        if hits:
            self.haveAkey = True
            self.key_hud.blit(self.game_sprites, (0, 0), (2730, 1170, 128, 128))

        # player in front of door
        hits = pygame.sprite.collide_rect(self.player, self.door)
        if hits and self.haveAkey:
            self.door_open = True
            self.door.switch('doorOpen_top')
            self.key_hud = pygame.Surface((128, 128), pygame.SRCALPHA, 32)
            self.haveAkey = False
        if hits and self.door_open and self.player.backing:
            print("Weldone " + self.saved_name + " you've succeed level " + self.level_loaded + "!")
            self.playing = False

    def events(self):
        # Game Loop - events
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not self.player.backing:
                    self.player.jump()
                if event.key == pygame.K_UP and not self.player.falling:
                    self.player.backing = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    self.player.jump_break()
                if event.key == pygame.K_UP:
                    self.player.backing = False

    def draw(self):
        # Game Loop - draw
        self.screen.fill(bgcolor)
        self.all_sprites.draw(self.screen)
        # To be sure player always in front
        self.screen.blit(self.player.image, self.player.rect)
        # Display HUD
        self.screen.blit(self.hud_head, (20,20))
        self.screen.blit(self.key_hud_empty, (70,-15))
        self.screen.blit(self.key_hud, (70,-15))
        #flip the display
        pygame.display.flip()

    def menu_display(self, d_screen):
        if d_screen == 'menu':
            self.screen.fill(bgcolor)
            self.screen.blit(self.menu, (0, 0))
            pygame.display.flip()
            self.menu_state = d_screen
            self.menu_handler()

        if d_screen == 'play':
            self.screen.fill(bgcolor)
            self.screen.blit(self.play, (0, 0))
            pygame.display.flip()
            self.menu_state = d_screen
            self.menu_handler()

        if d_screen == 'new_game':
            self.screen.fill(bgcolor)
            self.screen.blit(self.new_game, (0, 0))
            self.choice_player = pygame.Surface((80, 110))
            self.choice_player.fill(bgcolor)
            self.screen.blit(self.player_pick, (470, 337), PICK[int(self.data_player)])
            pygame.display.flip()
            self.menu_state = d_screen
            self.menu_handler()

        if d_screen == 'continue_game':
            self.screen.fill(bgcolor)
            self.screen.blit(self.continue_game, (0, 0))
            pygame.display.flip()
            self.menu_state = d_screen
            self.menu_handler()

    def menu_handler(self):
        self.waiting = True
        while self.waiting:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                #Kill the Window
                if event.type == pygame.QUIT:
                    self.waiting = False
                    self.running = False
                #handle mouse events in each menu screen
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 :
                        pos = event.pos
                        #play
                        if 428 < pos[0] < 596 and 225 < pos[1] < 286 and self.menu_state == 'menu':
                            self.menu_display('play')
                            self.waiting = False

                        #settings
                        if 371 < pos[0] < 658 and 376 < pos[1] < 432 and self.menu_state == 'menu':
                            print("SETTINGS")

                        #quit
                        if 437 < pos[0] < 585 and 542 < pos[1] < 591 and self.menu_state == 'menu':
                            self.waiting = False
                            self.running = False

                        #play - new Game
                        if 402 < pos[0] < 625 and 297 < pos[1] < 354 and self.menu_state == 'play':
                            self.menu_display('new_game')
                            self.waiting = False

                        #choose previous player - new game
                        if 425 < pos[0] < 453 and 385 < pos[1] < 420 and self.menu_state == 'new_game':
                            if self.data_player >= 0:
                                self.data_player -= 1
                                if self.data_player == -1:
                                    self.data_player = 4
                                self.screen.blit(self.choice_player, (470, 337))
                                pygame.display.flip()
                                self.screen.blit(self.player_pick, (470, 337), PICK[self.data_player])
                                pygame.display.flip()

                        #choose next player - new game
                        if 564 < pos[0] < 590 and 383 < pos[1] < 424 and self.menu_state == 'new_game':

                            if self.data_player <= 4:
                                self.data_player += 1
                                if self.data_player == 5:
                                    self.data_player = 0
                                self.screen.blit(self.choice_player, (470, 337))
                                pygame.display.flip()
                                self.screen.blit(self.player_pick, (470, 337), PICK[self.data_player])
                                pygame.display.flip()

                        #start - new game
                        if 458 < pos[0] < 576 and 484 < pos[1] < 542 and self.menu_state == 'new_game':
                            self.create_new_game()
                            self.waiting = False

                        #back to menu - new game
                        if 356 < pos[0] < 674 and 568 < pos[1] < 622 and self.menu_state == 'new_game':
                            self.menu_display('menu')
                            self.waiting = False

                        #continue game - play
                        if 359 < pos[0] < 666 and 418 < pos[1] < 474 and self.menu_state == 'play':
                            self.menu_display('continue_game')
                            self.waiting = False

                        #Username - continue game
                        if 392 < pos[0] < 622 and 335 < pos[1] < 392 and self.menu_state == 'continue_game':
                            self.load_game()
                            self.waiting = False

                        #back to menu - continue game
                        if 353 < pos[0] < 674 and 538 < pos[1] < 595 and self.menu_state == 'continue_game':
                            self.menu_display('menu')
                            self.waiting = False

                        #back to menu - play
                        if 353 < pos[0] < 674 and 538 < pos[1] < 595 and self.menu_state == 'play':
                            self.menu_display('menu')
                            self.waiting = False

    def victory_screen(self):
        #Victory
        self.screen.fill(bgcolor)
        pygame.display.flip()
        self.next_level = str(input("Are you sure you wanna play next level? It's way too hard for you! : y/n "))
        if self.next_level == 'y':
            self.save_game()
            if self.level_loaded == '7':
                print("Hum maybe you are smartest than you look after all!\nBut it's just the beginning, I'll be back!\nSee you soon " + self.saved_name + "!")
                self.running = False
            else:
                launch.game()
        if self.next_level == 'n':
            self.save_game()
            print("I knew it haha! Oh by the way your game as been saved!")
            self.running = False

if __name__ == '__main__':
    launch = UntitledGame()
    launch.menu_display('menu')
    launch.game()
    while launch.running:
        launch.victory_screen()

pygame.quit()

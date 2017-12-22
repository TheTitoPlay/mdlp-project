#!/usr/bin/env python
#
# Game for MDLP Project
#
#git@github.com:TheTitoPlay/mdlp-project.git
#https://github.com/TheTitoPlay/mdlp-project.git

import pygame
from settings import *
vec = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
    def __init__(self, game, selected_player, player_start_pos):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.walking = False
        self.jumping = False
        self.falling = False
        self.backing = False
        self.current_frame = 0
        self.last_update = 0
        self.load_sprites()
        self.image = self.stand_frames[0]
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(player_start_pos[0], player_start_pos[1])
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def load_sprites(self):
        self.stand_frames = [self.game.tilesheet.get_image(0,0,80,110),
                             self.game.tilesheet.get_image(400,220,80,110)]

        self.walk_frames_r = [self.game.tilesheet.get_image(80,110,80,110),
                              self.game.tilesheet.get_image(0,110,80,110)]

        self.walk_frames_l = []

        for frame in self.walk_frames_r:
             self.walk_frames_l.append(pygame.transform.flip(frame, True, False))

        self.jump_frame = self.game.tilesheet.get_image(80,0,80,110)
        self.jump_frame_l = pygame.transform.flip(self.jump_frame, True, False)

        self.fall = self.game.tilesheet.get_image(160,0,80,110)
        self.fall_l = pygame.transform.flip(self.fall, True, False)

        self.back = self.game.tilesheet.get_image(320,220,80,110)

    def jump_break(self):
        if self.jumping:
            if self.vel.y < -5:
                self.vel.y = -5

    def jump(self):
        # jump from plateform
        self.rect.x += 1
        hits = pygame.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        if hits and not self.jumping:
            self.jumping = True
            self.vel.y = -JUMP

    def update(self):
        self.animate()
        self.acc = vec(0, GRAVITY)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and not self.backing:
            self.acc.x = SPEED

        if keys[pygame.K_LEFT] and not self.backing:
            self.acc.x = -SPEED

        self.acc.x += self.vel.x * FRICTION
        self.vel += self.acc
        if abs(self.vel.x) < 0.1:
            self.vel.x = 0
        self.pos += self.vel + 0.5 * self.acc

        #Stop when hits screen sides
        if self.pos.x <= 40:
            self.pos.x = 40
            self.vel.x = 0

        if self.pos.x >= WIDTH - 40:
            self.pos.x = WIDTH - 40
            self.vel.x = 0

        self.rect.midbottom = self.pos

    def animate(self):
        now = pygame.time.get_ticks()
        if self.vel.x != 0:
            self.walking = True
        else:
            self.walking = False

        if self.walking:
            if now - self.last_update > 180:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.walk_frames_l)
                bottom = self.rect.bottom
                if self.vel.x > 0:
                    self.image = self.walk_frames_r[self.current_frame]
                else:
                    self.image = self.walk_frames_l[self.current_frame]

                self.rect = self.image.get_rect()
                self.rect.bottom = bottom

        if self.jumping:
            if self.vel.x > 0:
                self.image = self.jump_frame
            else:
                self.image = self.jump_frame_l

        if self.vel.y > 0:
            self.falling = True
        else:
            self.falling = False

        if self.falling:
            if self.vel.x >= 0:
                self.image = self.fall
            if self.vel.x < 0:
                self.image = self.fall_l

        if self.backing:
            self.image = self.back

        if not self.jumping and not self.walking and not self.falling and not self.backing:

            if now - self.last_update > 350:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.stand_frames)
                bottom = self.rect.bottom
                self.image = self.stand_frames[self.current_frame]
                self.rect = self.image.get_rect()
                self.rect.bottom = bottom

class PlayerSprites:
    def __init__(self, sprite_file):
        self.tilesheet = pygame.image.load(sprite_file).convert_alpha()
        self.tilesheet_l = (pygame.transform.flip(self.tilesheet, True, False))

    def get_image(self, x, y, width, height):
        image = pygame.Surface((width, height), pygame.SRCALPHA, 32)
        image.blit(self.tilesheet, (0, 0), (x, y, width, height))
        return image

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
        if keys[pygame.K_RIGHT]:
            self.acc.x = SPEED

        if keys[pygame.K_LEFT]:
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

        if not self.jumping and not self.walking and not self.falling:

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

        '''## Create Actions List
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
                return self._walk[self._walks]'''

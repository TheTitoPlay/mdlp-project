import pygame
from game_sprites import *


class Sprite(pygame.sprite.Sprite):
    def __init__(self, image, sprite_type, sprite_coord):
        pygame.sprite.Sprite.__init__(self)
        self.game_sprites = GameSprites()
        self.sheet = image
        self.image = self.game_sprites.get_image_sprite(image, self.game_sprites.get_resources(sprite_type))

        self.rect = self.image.get_rect()
        self.rect.x = sprite_coord[0]
        self.rect.y = sprite_coord[1]

class DynamicSprite(Sprite):
    def switch(self, sprite_type_switch):
        self.image = self.game_sprites.get_image_sprite(self.sheet, self.game_sprites.get_resources(sprite_type_switch))

class Hud():
    def create(self, image, hud_type):
        self.hud_surface = image.get_rect()
        


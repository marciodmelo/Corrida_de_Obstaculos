#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.key

from code.const import WIN_WIDTH, ENTITY_SPEED, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_RIGHT, \
    PLAYER_KEY_LEFT
from code.entity import Entity


class Player(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.top >= 275:
                self.rect.centery -= 5
        if pressed_key[PLAYER_KEY_DOWN[self.name]] and self.rect.top <= 340:
                self.rect.centery += 5
        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
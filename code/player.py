#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.key

from code.const import WIN_WIDTH, WIN_HEIGHT, ENTITY_SPEED
from code.entity import Entity


class Player(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_UP] and self.rect.top >= 370:
                self.rect.centery -= 35
        if pressed_key[pygame.K_DOWN] and self.rect.top <= 335:
                self.rect.centery += 35
        if pressed_key[pygame.K_RIGHT] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]
        if pressed_key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
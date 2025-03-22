#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.key

from code.const import WIN_WIDTH, WIN_HEIGHT
from code.entity import Entity


class Player(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.player_pos = position[1]

    def move(self, ):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_UP] and self.rect.top > -WIN_HEIGHT:
            for i in range(10):
                self.rect.centery -= 1
        else:
            self.rect.centery = self.player_pos
        if pressed_key[pygame.K_RIGHT] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += 5
        if pressed_key[pygame.K_LEFT]:
            self.rect.centerx -= 5
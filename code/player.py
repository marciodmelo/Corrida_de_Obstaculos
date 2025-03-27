#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.key
from code.const import WIN_WIDTH, ENTITY_SPEED, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_RIGHT, PLAYER_KEY_LEFT
from code.entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple[int, int]):
        """Inicializa o jogador na posição especificada."""
        super().__init__(name, position)

    def move(self) -> None:
        """Move o jogador com base nas teclas pressionadas."""
        pressed_key = pygame.key.get_pressed()

        if self.rect.top >= 275 and pressed_key[PLAYER_KEY_UP[self.name]]:
            self.rect.centery -= 5
        if self.rect.top <= 340 and pressed_key[PLAYER_KEY_DOWN[self.name]]:
            self.rect.centery += 5
        if self.rect.right < WIN_WIDTH and pressed_key[PLAYER_KEY_RIGHT[self.name]]:
            self.rect.centerx += ENTITY_SPEED[self.name]
        if self.rect.left > 0 and pressed_key[PLAYER_KEY_LEFT[self.name]]:
            self.rect.centerx -= ENTITY_SPEED[self.name]

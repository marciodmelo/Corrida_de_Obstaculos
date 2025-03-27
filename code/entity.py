#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
import pygame.image
from code.const import ENTITY_HEALTH, ENTITY_DAMAGE, ENTITY_SCORE

class Entity(ABC):
    def __init__(self, name: str, position: tuple[int, int]):
        """Inicializa a entidade com imagem, posição e atributos de jogo."""
        self.name: str = name
        self.surf = pygame.image.load(f'./asset/{name}.png').convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed: int = 0
        self.health: int = ENTITY_HEALTH[self.name]
        self.damage: int = ENTITY_DAMAGE[self.name]
        self.score: int = ENTITY_SCORE[self.name]
        self.last_dmg: str = 'None'  # Último causador de dano

    @abstractmethod
    def move(self):
        """Método abstrato para movimento da entidade."""
        pass

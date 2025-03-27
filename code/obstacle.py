#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.const import ENTITY_SPEED
from code.entity import Entity


class Obstacle(Entity):
    def __init__(self, name: str, position: tuple[int, int]):
        """Inicializa um obstáculo na posição especificada."""
        super().__init__(name, position)

    def move(self) -> None:
        """Move o obstáculo horizontalmente conforme a velocidade definida."""
        self.rect.centerx += ENTITY_SPEED[self.name]

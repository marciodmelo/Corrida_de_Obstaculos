#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
from code.background import Background
from code.const import WIN_WIDTH, WIN_HEIGHT
from code.obstacle import Obstacle
from code.player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(6):
                    list_bg.append(Background(f'Level1Bg{i}', (0,0)))
                    list_bg.append(Background(f'Level1Bg{i}', (-WIN_WIDTH, 0)))
                return list_bg
            case 'Player':
                return Player('Player', (WIN_WIDTH-200, 335))
            case 'Obstacle':
                return  Obstacle('Obstacle', (-50, random.randint(335, 405)))


#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import pygame.display
from pygame import Surface, Rect, KEYDOWN, K_ESCAPE
from pygame.font import Font
from code.const import C_WHITE, WIN_HEIGHT, EVENT_OBSTACLE, MENU_OPTION, C_GREEN, C_CYAN, EVENT_TIMEOUT, TIMEOUT_STEP, \
    TIMEOUT_LEVEL, SPAWN_TIME_PLAYER1, C_BLACK, C_RED, SPAWN_TIME_PLAYER2
from code.entity import Entity
from code.entityFactory import EntityFactory
from code.entityMediator import EntityMediator
from code.player import Player


class Level:
    def __init__(self, window: Surface, name: str, game_mode: str, player_score: list[int]):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.timeout = TIMEOUT_LEVEL
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg'))
        player = EntityFactory.get_entity('Player1')
        player.score = player_score[0]
        self.entity_list.append(player)
        pygame.time.set_timer(EVENT_OBSTACLE, SPAWN_TIME_PLAYER1)
        if game_mode == MENU_OPTION[1]:
            pygame.time.set_timer(EVENT_OBSTACLE, SPAWN_TIME_PLAYER2)
            player = EntityFactory.get_entity('Player2')
            player.score = player_score[1]
            self.entity_list.append(player)
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)

    def run(self, player_score: list[int]):
        pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

                if ent.name == 'Player1':
                    self.level_text(14, f'Player1 - Ponto(s): {ent.score}', C_RED, (10, 25))
                if ent.name == 'Player2':
                    self.level_text(14, f'Player2 - Ponto(s): {ent.score}', C_CYAN, (10, 45))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return

                if event.type == EVENT_OBSTACLE:
                    self.entity_list.append(EntityFactory.get_entity('Obstacle'))

                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout == 0:
                        for ent in self.entity_list:
                            if isinstance(ent, Player) and ent.name == 'Player1':
                                player_score[0] = ent.score
                            if isinstance(ent, Player) and ent.name == 'Player2':
                                player_score[1] = ent.score
                        return True

            self.level_text(14, f'Tempo de Jogo: {self.timeout / 1000 :.1f}s', C_BLACK, (10, 5))
            pygame.display.flip()

            # Collisions
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)

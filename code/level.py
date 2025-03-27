#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import pygame
from pygame import Surface, Rect, KEYDOWN, K_ESCAPE
from pygame.font import Font
from code.const import EVENT_OBSTACLE, MENU_OPTION, C_CYAN, EVENT_TIMEOUT, TIMEOUT_STEP, \
    TIMEOUT_LEVEL, SPAWN_TIME_PLAYER1, C_BLACK, C_RED, SPAWN_TIME_PLAYER2, F_FONT_1
from code.entity import Entity
from code.entityFactory import EntityFactory
from code.entityMediator import EntityMediator
from code.player import Player

class Level:
    def __init__(self, window: Surface, name: str, game_mode: str, player_score: list[int]):
        """Inicializa o nível do jogo com configurações base e entidades."""
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.timeout = TIMEOUT_LEVEL
        self.entity_list: list[Entity] = []

        # Adiciona o fundo e o jogador ao nível
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg'))
        player = EntityFactory.get_entity('Player1')
        player.score = player_score[0]
        self.entity_list.append(player)

        # Configura o timer para os obstáculos com base no jogador
        pygame.time.set_timer(EVENT_OBSTACLE, SPAWN_TIME_PLAYER1)

        # Se for o modo multiplayer, adiciona o segundo jogador
        if game_mode == MENU_OPTION[1]:
            pygame.time.set_timer(EVENT_OBSTACLE, SPAWN_TIME_PLAYER2)
            player = EntityFactory.get_entity('Player2')
            player.score = player_score[1]
            self.entity_list.append(player)

        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)

    def run(self, player_score: list[int]) -> bool:
        """Executa o loop do nível, atualizando a tela e verificando eventos."""
        # Inicia a música do nível
        pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        pygame.mixer_music.play(-1)

        clock = pygame.time.Clock()
        while True:
            clock.tick(60)

            # Desenha todas as entidades no nível
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

                # Atualiza a pontuação dos jogadores
                if ent.name == 'Player1':
                    self.level_text(14, f'Player1 - Ponto(s): {ent.score}', C_RED, (10, 25))
                if ent.name == 'Player2':
                    self.level_text(14, f'Player2 - Ponto(s): {ent.score}', C_CYAN, (10, 45))

            # Captura eventos do jogo
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return False  # Retorna False ao pressionar ESC para sair do nível

                if event.type == EVENT_OBSTACLE:
                    # Adiciona um novo obstáculo ao nível
                    self.entity_list.append(EntityFactory.get_entity('Obstacle'))

                if event.type == EVENT_TIMEOUT:
                    # Atualiza o tempo e verifica se o nível acabou
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout == 0:
                        for ent in self.entity_list:
                            if isinstance(ent, Player):
                                if ent.name == 'Player1':
                                    player_score[0] = ent.score
                                elif ent.name == 'Player2':
                                    player_score[1] = ent.score
                        return True  # Retorna True quando o tempo acaba

            # Exibe o tempo de jogo restante
            self.level_text(14, f'Tempo de Jogo: {self.timeout / 1000 :.1f}s', C_BLACK, (10, 5))
            pygame.display.flip()

            # Verifica as colisões
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        """Desenha o texto no nível (pontuação e tempo)."""
        text_font: Font = pygame.font.SysFont(name=F_FONT_1, size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
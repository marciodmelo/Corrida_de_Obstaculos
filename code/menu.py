#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import sys  # Importado para saída segura
from pygame import K_ESCAPE
from code.const import WIN_WIDTH, MENU_OPTION, C_RED, C_BLACK, F_FONT_1


class Menu:
    """Classe responsável pelo menu principal do jogo."""

    def __init__(self, window):
        """Inicializa o menu e carrega a imagem de fundo."""
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        """Executa o loop do menu, permitindo navegação e seleção de opções."""
        menu_option = 0

        # Carrega e toca a música do menu em loop
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)

        while True:
            # Renderiza o fundo do menu
            self.window.blit(source=self.surf, dest=self.rect)

            # Renderiza as opções do menu
            for i, option in enumerate(MENU_OPTION):
                color = C_RED if i == menu_option else C_BLACK
                self.menu_text(20 if i == menu_option else 17, option, color, ((WIN_WIDTH / 2), 190 + 22 * i))

            pygame.display.flip()

            # Captura eventos do teclado e da janela
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key in [pygame.K_DOWN, pygame.K_UP]:
                        # Alterna entre as opções do menu
                        menu_option = (menu_option + (1 if event.key == pygame.K_DOWN else -1)) % len(MENU_OPTION)
                    elif event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        """Renderiza o texto do menu na tela."""
        try:
            text_font = pygame.font.SysFont(F_FONT_1, text_size)
        except pygame.error:
            # Caso a fonte "Impact" não esteja disponível, usa uma fonte padrão
            text_font = pygame.font.Font(None, text_size)

        text_surf = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
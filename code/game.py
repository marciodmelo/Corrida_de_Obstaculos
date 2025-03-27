import pygame
import sys  # Para garantir a saída segura

from code.const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.level import Level
from code.menu import Menu
from code.score import Score

class Game:
    def __init__(self):
        """Inicializa o jogo e configura a janela."""
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        """Executa o loop principal do jogo, gerenciando menu e pontuação."""
        while True:
            score = Score(self.window)
            menu = Menu(self.window)
            menu_return = menu.run()

            # Se o jogador escolher jogar ou continuar
            if menu_return in [MENU_OPTION[0], MENU_OPTION[1]]:
                player_score = [0, 0]
                level = Level(self.window, 'Level1', menu_return, player_score)
                level_return = level.run(player_score)

                if level_return:
                    # Salva a pontuação após o nível
                    score.save(menu_return, player_score)

            # Se o jogador escolher ver a pontuação
            elif menu_return == MENU_OPTION[2]:
                score.show()

            # Se o jogador escolher sair
            elif menu_return == MENU_OPTION[3]:
                pygame.quit()
                sys.exit()

            # Caso haja outro retorno inválido (aqui é redundante, mas pode ser útil)
            else:
                pygame.quit()
                sys.exit()
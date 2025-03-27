import sys
from datetime import datetime
import pygame
from pygame import Surface, Rect, KEYDOWN, K_RETURN, K_BACKSPACE, K_ESCAPE
from pygame.font import Font
from code.DBProxy import DBProxy
from code.const import C_YELLOW, SCORE_POS, MENU_OPTION, C_WHITE, C_RED, F_FONT_1


class Score:
    def __init__(self, window: Surface):
        """Inicializa a classe Score."""
        self.window = window
        self.surf = pygame.image.load('./asset/ScoreBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        self.db_proxy = DBProxy('DBScore')

    def save(self, game_mode: str, player_score: list[int]):
        """Salva a pontuação do jogador no banco de dados."""
        pygame.mixer_music.load('./asset/Score.mp3')
        pygame.mixer_music.play(-1)
        name = ''
        score = max(player_score)  # Obtém a maior pontuação entre os jogadores

        while True:
            self.window.blit(self.surf, self.rect)
            self.score_text(48, 'VOCÊ VENCEU!!' if game_mode == MENU_OPTION[0] else f'VOCÊ VENCEU PLAYER{player_score.index(score) + 1}!!',
                            C_YELLOW, SCORE_POS['Title'])
            self.score_text(20, 'Digite seu nome com até 4 letras:', C_WHITE, SCORE_POS['EnterName'])
            self.score_text(20, name, C_RED, SCORE_POS['Name'])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
                    if event.key == K_RETURN and len(name) == 4:
                        self.db_proxy.save({'name': name, 'score': score, 'date': get_formatted_date()})
                        self.show()
                        return
                    elif event.key == K_BACKSPACE:
                        name = name[:-1]
                    elif len(name) < 4:
                        name += event.unicode

            pygame.display.flip()

    def show(self):
        """Exibe o ranking com as 10 melhores pontuações."""
        pygame.mixer_music.load('./asset/Score.mp3')
        pygame.mixer_music.play(-1)
        self.window.blit(self.surf, self.rect)
        self.score_text(48, 'TOP 10', C_YELLOW, SCORE_POS['Title'])
        self.score_text(20, 'NOME ----- PONTOS ----- DATA/HORA', C_WHITE, SCORE_POS['Label'])

        list_score = self.db_proxy.retrieve_top10()

        for idx, (id_, name, score, date) in enumerate(list_score):
            self.score_text(20, f'{name} ---- {score} ---- {date}', C_YELLOW, SCORE_POS[idx])

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    return

            pygame.display.flip()

    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        """Renderiza o texto na tela."""
        text_font: Font = pygame.font.SysFont(name=F_FONT_1, size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)


def get_formatted_date() -> str:
    """Retorna a data formatada como 'HH:MM - DD/MM/YY'."""
    return datetime.now().strftime("%H:%M - %d/%m/%y")

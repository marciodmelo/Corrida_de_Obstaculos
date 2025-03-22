# CONST
# C
import pygame

COLOR_ORANGE = (255,128,0)
COLOR_WHITE = (255,255,255)
COLOR_YELlOW = (255, 234, 0)
COLOR_BLACK = (0,0,0)
COLOR_RED = (255,0,0)

# E
ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 3,
    'Level1Bg3': 4,
    'Level1Bg4': 5,
    'Level1Bg5': 6,
    'Player1': 5,
    'Player2': 5,
    'Obstacle': 6,
}

EVENT_OBSTACLE = pygame.USEREVENT + 1

# M
MENU_OPTION = (
    'New Game - 1 Player',
    'New Game - 2 Player - COOPERATIVE',
    'New Game - 2 Player - COMPETITIVE',
    'SCORE',
    'Exit'
)

# P
PLAYER_KEY_UP = {'Player1': pygame.K_UP, 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN, 'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT, 'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT, 'Player2': pygame.K_d}

# W
WIN_WIDTH = 800
WIN_HEIGHT = 450
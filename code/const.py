# CONST
# C
import pygame

C_ORANGE = (255, 128, 0)
C_WHITE = (255, 255, 255)
C_YELlOW = (255, 234, 0)
C_BLACK = (0, 0, 0)
C_RED = (255, 0, 0)
C_GREEN = (0,128,0)
C_CYAN = (0,128,128)

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

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level1Bg5': 999,
    'Player1': 300,
    'Player2': 300,
    'Obstacle': 1,
}

ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Player1': 1,
    'Player2': 1,
    'Obstacle': 1,
}

ENTITY_SCORE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Player1': 0,
    'Player2': 0,
    'Obstacle': 1,
}

EVENT_TIMEOUT = pygame.USEREVENT + 2

# M
MENU_OPTION = (
    'New Game - 1 Player',
    'New Game - 2 Player',
    'Score',
    'Exit',
)

# P
PLAYER_KEY_UP = {'Player1': pygame.K_UP, 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN, 'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT, 'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT, 'Player2': pygame.K_d}

# S
SPAWN_TIME = 1000

# T
TIMEOUT_STEP = 100
TIMEOUT_LEVEL = 20000

# W
WIN_WIDTH = 800
WIN_HEIGHT = 450

# S
SCORE_POS = {
    'Title': (WIN_WIDTH / 2, 140),
    'EnterName': (WIN_WIDTH / 2, 170),
    'Label': (WIN_WIDTH / 2, 210),
    'Name': (WIN_WIDTH / 2, 190),
    0: (WIN_WIDTH / 2, 240),
    1: (WIN_WIDTH / 2, 260),
    2: (WIN_WIDTH / 2, 280),
    3: (WIN_WIDTH / 2, 300),
    4: (WIN_WIDTH / 2, 320),
    5: (WIN_WIDTH / 2, 340),
    6: (WIN_WIDTH / 2, 360),
    7: (WIN_WIDTH / 2, 380),
    8: (WIN_WIDTH / 2, 400),
    9: (WIN_WIDTH / 2, 420),
}
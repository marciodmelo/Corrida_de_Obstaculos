import pygame

# Cores
COLOR_ORANGE = (255, 128, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (255, 234, 0)

# Velocidades das entidades
ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 3,
    'Level1Bg3': 4,
    'Level1Bg4': 5,
    'Level1Bg5': 6,
    'Player': 5,
    'Obstacle': 6,
}

# Evento para criação de obstáculos
EVENT_OBSTACLE = pygame.USEREVENT + 1

# Opções do menu
MENU_OPTION = (
    'New Game',
    'Exit'
)

# Dimensões da tela
WIN_WIDTH = 800
WIN_HEIGHT = 450

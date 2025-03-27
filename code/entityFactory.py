import random
from code.background import Background
from code.const import WIN_WIDTH
from code.obstacle import Obstacle
from code.player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str) -> list | Player | Obstacle:
        """Cria e retorna instâncias de entidades com base no nome informado."""

        if entity_name == 'Level1Bg':
            return [Background(f'Level1Bg{i}', (pos, 0)) for i in range(6) for pos in (0, -WIN_WIDTH)]

        match entity_name:
            case 'Player1':
                return Player('Player1', (WIN_WIDTH - 220, 300))
            case 'Player2':
                return Player('Player2', (WIN_WIDTH - 200, 345))
            case 'Obstacle':
                return Obstacle('Obstacle', (0, random.randint(335, 400)))

        raise ValueError(f"Entidade '{entity_name}' não reconhecida.")  # Evita retornos inesperados

from code.const import WIN_WIDTH
from code.entity import Entity
from code.obstacle import Obstacle
from code.player import Player

class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity) -> None:
        """Verifica se um obstáculo saiu da tela e deve ser removido."""
        if isinstance(ent, Obstacle) and ent.rect.right > WIN_WIDTH:
            ent.health = 0

    @staticmethod
    def __verify_collision_entity(ent1: Entity, ent2: Entity) -> None:
        """Verifica e aplica dano em caso de colisão entre jogador e obstáculo."""
        if {type(ent1), type(ent2)} == {Player, Obstacle}:  # Confirma se um é Player e o outro é Obstacle
            if (ent1.rect.left < ent2.rect.right <= ent1.rect.left + 10 and
                    ent1.rect.bottom - 30 <= ent2.rect.top + (ent2.rect.height / 2) <= ent1.rect.bottom):

                ent1.health -= ent2.damage
                ent2.health -= ent1.damage
                ent1.last_dmg, ent2.last_dmg = ent2.name, ent1.name

    @staticmethod
    def give_score(obstacle: Obstacle, entity_list: list[Entity]) -> None:
        """Atribui pontos ao jogador correspondente quando um obstáculo é destruído."""
        for ent in entity_list:
            if ent.name == obstacle.last_dmg:
                ent.score += obstacle.score

    @staticmethod
    def verify_collision(entity_list: list[Entity]) -> None:
        """Verifica todas as colisões entre entidades da lista."""
        for i, entity1 in enumerate(entity_list):
            EntityMediator.__verify_collision_window(entity1)
            for entity2 in entity_list[i + 1:]:  # Evita verificações duplicadas
                EntityMediator.__verify_collision_entity(entity1, entity2)

    @staticmethod
    def verify_health(entity_list: list[Entity]) -> None:
        """Remove entidades sem vida e atribui pontos caso seja um obstáculo."""
        for ent in entity_list[:]:  # Iterar sobre uma cópia para evitar erro de remoção
            if ent.health <= 0:
                if isinstance(ent, Obstacle):
                    EntityMediator.give_score(ent, entity_list)
                entity_list.remove(ent)

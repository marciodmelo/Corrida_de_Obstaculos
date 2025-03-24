from code.const import WIN_WIDTH
from code.entity import Entity
from code.obstacle import Obstacle
from code.player import Player


class EntityMediator:
    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Obstacle):
            if ent.rect.right > WIN_WIDTH:
                ent.health = 0

    @staticmethod
    def __verify_collision_entity(ent1, ent2):
        valid_interation = False
        if isinstance(ent1, Player) and isinstance(ent2, Obstacle):
            valid_interation = True
        elif isinstance(ent1, Obstacle) and isinstance(ent2, Player):
            valid_interation = True

        if valid_interation:
            if (ent1.rect.left < ent2.rect.right <= ent1.rect.left + 10 and
                    ent1.rect.bottom - 30 <= ent2.rect.top + (
                            ent2.rect.height / 2) <= ent1.rect.bottom):

                ent1.health -= ent2.damage
                ent2.health -= ent1.damage
                ent1.last_dmg = ent2.name
                ent2.last_dmg = ent1.name

    @staticmethod
    def give_score(obstacle: Obstacle, entity_listy: list[Entity]):
        if obstacle.last_dmg == 'Player1':
            for ent in entity_listy:
                if ent.name == 'Player1':
                    ent.score += obstacle.score
        elif obstacle.last_dmg == 'Player2':
            for ent in entity_listy:
                if ent.name == 'Player2':
                    ent.score += obstacle.score

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)
            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                if isinstance(ent, Obstacle):
                    EntityMediator.give_score(ent, entity_list)
                entity_list.remove(ent)

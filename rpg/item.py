import pygame


class Item:
    def __init__(self, name: str, level: int, ability: str, icon: pygame.surface):
        self.name = name
        self.level = level
        self.ability = ability
        self.icon = icon

    def get_cost(self):
        cost = self.level * 50
        return cost


class Consumable(Item):
    pass


class Equipable(Item):
    pass


class Weapon(Equipable):
    def get_damage(self) -> int:
        return self.level * 5


class Armor(Equipable):
    def get_damage_reduction(self) -> int:
        return self.level * 4

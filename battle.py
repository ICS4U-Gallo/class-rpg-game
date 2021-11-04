import random
from typing import List

from character import Character


class Battle:
    def __init__(self, player_party: List[Character],
                 enemy_party: List[Character]) -> None:
        self._player_party = player_party
        self._enemy_party = enemy_party
        self._turn = 0
        self._turn_order = []
        self._init_order()
    
    def _init_order(self) -> None:
        self._turn_order = self._player_party + self._enemy_party
        random.shuffle(self._turn_order)
    
    def get_current_character(self) -> Character:
        character_index = self._turn % len(self._turn_order)
        return self._turn_order[character_index]




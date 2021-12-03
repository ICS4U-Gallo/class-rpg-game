from typing import List

import pygame
from pygame.constants import MOUSEBUTTONDOWN

from .view import View
from .shop_screen import ShopScreen


class TitleScreen(View):
    def event_loop(self, events: List[pygame.event.Event]) -> None:
        for event in events:
            if event.type == MOUSEBUTTONDOWN:
                self.parent.set_child(ShopScreen())

    def update(self) -> None:
        pass

    def draw(self, screen: pygame.Surface) -> None:
        screen.fill((0, 0, 128))

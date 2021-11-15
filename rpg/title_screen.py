from typing import List

import pygame

from .view import View


class TitleScreen(View):
    def event_loop(self, events: List[pygame.event.Event]) -> None:
        for event in events:
            print(event)

    def update(self) -> None:
        pass

    def draw(self, screen: pygame.Surface) -> None:
        screen.fill((0, 0, 128))

from typing import List

import pygame

from .view import View


class ShopScreen(View):
    def __init__(self):
        some_font = pygame.font.SysFont('Arial', 50)

        # in loop
        self.title_text = some_font.render('Shop', True, (0, 0, 0))

    def event_loop(self, events: List[pygame.event.Event]) -> None:
        for event in events:
            pass

    def update(self) -> None:
        pass

    def draw(self, screen: pygame.Surface) -> None:
        screen.fill((255, 255, 255))
        screen_width = screen.get_width()
        text_width = self.title_text.get_width()
        screen.blit(self.title_text, (screen_width//2 - text_width//2, 50))

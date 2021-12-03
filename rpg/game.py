import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT

from .view import View
from .title_screen import TitleScreen


class Game(View):
    def __init__(self):
        self.WIDTH = 1280
        self.HEIGHT = 720
        self.SIZE = (self.WIDTH, self.HEIGHT)

        self.screen = pygame.display.set_mode(self.SIZE)
        self.clock = pygame.time.Clock()

        self.child = TitleScreen(self)
    
    def set_child(self, child: View) -> None:
        self.child = child

    def run(self):
        running = True
        while running:
            events = pygame.event.get()
            for event in events:
                if event.type == QUIT:
                    running = False
            
            self.child.event_loop(events)
            self.child.update()
            self.child.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(30)


        pygame.quit()

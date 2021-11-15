import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT

from .view import View


class Game:
    def __init__(self, view: View):
        self.WIDTH = 1280
        self.HEIGHT = 720
        self.SIZE = (self.WIDTH, self.HEIGHT)

        self.screen = pygame.display.set_mode(self.SIZE)
        self.clock = pygame.time.Clock()

        self.current_view = view


    def run(self):
        running = True
        while running:
            events = pygame.event.get()
            for event in events:
                if event.type == QUIT:
                    running = False
            
            self.current_view.event_loop(events)
            self.current_view.update()
            self.current_view.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(30)


        pygame.quit()

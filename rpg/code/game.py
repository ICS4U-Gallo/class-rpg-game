import pygame
from config import *
from pygame.locals import QUIT

class Game:
    def __init__(self, view):
        print("running")
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
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
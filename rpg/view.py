from typing import List

import pygame


class View:
    """A pseudo-interface for views that can be used in the game class."""

    def event_loop(self, events: List[pygame.event.Event]) -> None:
        """View-specific event loop for key-bindings"""
        raise NotImplementedError("You need to override the 'event_loop' method in every class inheriting from the View class.")

    def update(self) -> None:
        """Update the view's state"""
        raise NotImplementedError("You need to override the 'update' method in every class inheriting from the View class.")
    
    def draw(self, screen: pygame.Surface) -> None:
        """Draw the view's contents."""
        raise NotImplementedError("You need to override the 'draw' method in every class inheriting from the View class.")

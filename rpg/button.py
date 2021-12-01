import pygame
from typing import Union, Optional, List, Tuple, Callable


def load_surface(surface_ref: Union[str, pygame.Surface, Tuple[int, int, int]]) -> Optional[pygame.Surface]:
    """Load a pygame surface

    Args:
        surface_ref: the file path to the surface OR a pygame surface OR a rgb color

    Returns:
        the loaded surface, None if fails
    """
    try:
        if type(surface_ref) == str:
            return pygame.image.load(surface_ref)
        elif type(surface_ref) == pygame.Surface:
            return pygame.Surface
        elif type(surface_ref) in [tuple, list]:
            surface = pygame.Surface((1, 1))
            pygame.draw.rect(surface, surface_ref, [0, 0, 1, 1])
            return surface
        else:
            return None
    except:
        return None


class Button:

    def __init__(self, x: float, y: float,
                 image_default: Union[str, pygame.Surface, Tuple[int, int, int]],
                 image_hover=None,
                 image_click=None,
                 width: float = None,
                 height: float = None):
        self.pos_x = x
        self.pos_y = y
        self.width = width
        self.height = height
        self.onclicks = []

        if image_hover == None:
            image_hover = image_default
        if image_click == None:
            image_click = image_hover
        self.image_default = load_surface(image_default)
        self.image_hover = load_surface(image_hover)
        self.image_click = load_surface(image_click)
        self._image = self.image_default

        if self.width == None or self.height == None:
            if self._image != None:
                self.width = self._image.get_width()
                self.height = self._image.get_height()
            else:
                self.width = self.height = 1

    def draw(self, surface: pygame.Surface) -> bool:
        """Draw the button on screen

        Args:
            surface: the surface to draw, e.g. screen

        Returns:
            True if drawn successfully, False otherwise
        """
        rect = pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)
        if self._image == None:
            return False
        image = pygame.transform.scale(self._image, (self.width, self.height))
        surface.blit(image, rect)
        return True

    def is_hover(self, mouse_x: float, mouse_y: float) -> bool:
        """Test if mouse position is on the button

        Args:
            mouse_x: x-coordinate of the mouse
            mouse_y: y-coordinate of the mouse

        Returns:
            True if mouse is on the button, False otherwise
        """
        return pygame.Rect(self.pos_x, self.pos_y, self.width, self.height).collidepoint(mouse_x, mouse_y)

    def mouse_move(self, mouse_x: float, mouse_y: float) -> None:
        """Call this when mouse moved"""
        if self.is_hover(mouse_x, mouse_y):
            self._image = self.image_hover
        else:
            self._image = self.image_default

    def mouse_click(self, mouse_x: float, mouse_y: float):
        """Call this when mouse button down"""
        if self.is_hover(mouse_x, mouse_y):
            self._image = self.image_click
            for fun in self.onclicks:
                fun()

    def add_onclick(self, onclick: Callable) -> None:
        """Add a function that will be called once the mouse clicks

        Args:
            onclick: a callable object (like a function) with zero parameters
        """
        self.onclicks.append(onclick)

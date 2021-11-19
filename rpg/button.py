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
    pos_x: float
    pos_y: float
    width: float
    height: float
    image_default: pygame.Surface
    image_click: pygame.Surface
    _image: pygame.Surface
    onclicks: List[Callable]

    def __init__(self, x: float, y: float, w: float, h: float,
                 image_default=None,
                 image_hover=None,
                 image_click=None):
        self.pos_x = x
        self.pos_y = y
        self.width = w
        self.height = h
        self.onclicks = []

        if image_hover == None:
            image_hover = image_default
        if image_click == None:
            image_click = image_hover
        self.image_default = load_surface(image_default)
        self.image_hover = load_surface(image_hover)
        self.image_click = load_surface(image_click)
        self._image = self.image_default

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
        if 0 <= mouse_x-self.pos_x < self.width and 0 <= mouse_y-self.pos_y < self.height:
            return True
        return False

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

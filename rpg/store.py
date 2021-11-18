
class Item:
    # def __init__(self, name: str) -> None:
    #     self.name = name
        pass


class ShopListMenu():
    # done b
    def __init__(self, items: List[Item], selected_index: int, type_items: str) -> None:
        self.items = items
        self.selected_index = selected_index
        self.type_items = type_items
    # done b
    
    def select_next(self) -> None:
        """Moves the selected index up one item."""
        max_index = len(self.items) - 1
        self.selected_index = min(self.selected_index + 1,max_index)

    # done b
    def select_previous(self) -> None:
        """Moves the selected index down one item."""
        self.selected_index = max(self.selected_index - 1, 0)

    # done b
    def get_selected(self) -> Item:
        """Returns the item that matches the selected index from the list of items.

        Returns:
            The item selected.
        """
        return self.items[self.selected_index]

    # def draw(self, screen):

class Store:
    # m
    def __init__(self, weapons: ShopListMenu, armor: ShopListMenu, consumables: ShopListMenu, title: str) -> None:
        self.weapons = weapons
        self.armor = armor
        self.consumables = consumables
        self.title = title

from typing import List

class Item:

    def __init__(self, name: str):
        self._name = name


    def __str__(self):
        return f"{self._name}"

class ShopListMenu():

    def __init__(self, items: List[Item], selected_index: int, type_items: str) -> None:
        self._items = items
        self._selected_index = selected_index
        self._type_items = type_items


    def __str__(self):
        return f"{self._type_items} list containing {self._items}."


    def select_next(self) -> None:
        """Moves the selected index up one item."""
        max_index = len(self._items) - 1
        self._selected_index = min(self._selected_index + 1, max_index)


    def select_previous(self) -> None:
        """Moves the selected index down one item."""
        self._selected_index = max(self_.selected_index - 1, 0)


    def get_selected(self) -> Item:
        """Returns the item that matches the selected index from the list of items.
        
        Returns:
            The item selected.
        """
        return self._items[self._selected_index]


    def set_type_items(self, title: str) -> None:
        """Sets the title of the shop list menu.
        
        Args:
            title: new title for the shop list menu,
        """
        if len(title) > 10:
            raise ValueError("The title of the ShopListMenu cannot be more than 10 characters long.")
        self._type_items = title
    

    def get_type_items(self) -> str:
        """Returns the type of items the shop list menu holds.
        
        Returns:
            String containing the title of the shop list menu.
        """
        return self._type_items


    def add_item(self, item: Item) -> None:
        """Adds an item to the list of items.
        
        Args:
            item: Item object to be added to list of items.
        """
        self._items.append(item)


    def remove_item(self, item: Item) -> None:
        """Removes and item from the list of items.
    
        Args:
        item: Item object to be removed from the list of items.
        """
        for i in self._items:
            if i == item:
                self._items.remove(i)


    def get_items_names(self) -> str:
        """Returns a string with the names of the items in the list.
        
        Returns: string with readable names of the items.
        """
        list_names = ""
        for i in self._items:
            list_names = list_names + "\n"+ i._name

        return list_names

    
    def draw(self, screen):
        pass

class Store:

    def __init__(self, weapons: ShopListMenu, armor: ShopListMenu, consumables: ShopListMenu, title: str) -> None:
        self._weapons = weapons
        self._armor = armor
        self._consumables = consumables
        self._title = title


    def get_all_items(self) -> str:
        """Returns a formatted string of all the items in a store.
        
        Returns:
            Master list of items in a store
        """
        weapons = self._weapons.get_items_names()
        armor = self._armor.get_items_names()
        consumables = self._consumables.get_items_names()
        return f"{self._title} has these items:\n\nWEAPONS{weapons}\n\nARMOR{armor}\n\nCONSUMABLES{consumables}"

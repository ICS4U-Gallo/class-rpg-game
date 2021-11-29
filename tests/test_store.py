import pytest
from main import ShopListMenu
from main import Item
from main import Store

# done b
def test_shop_list_menu_attributes():
    item1 = Item()
    item2 = Item()
    item3 = Item()
    shop = ShopListMenu([item1, item2, item3], 0, "consumables")
    assert shop.items == [item1, item2, item3]
    assert shop.selected_index == 0
    assert shop.type_items == "consumables"
    

# done b
def test_get_selected():
    item1 = Item()
    item2 = Item()
    item3 = Item()
    shop = ShopListMenu([item1, item2, item3], 0, "consumables")
    assert shop.get_selected() == item1

    shop = ShopListMenu([item1, item2, item3], 1, "consumables")
    assert shop.get_selected() == item2

    shop = ShopListMenu([item1, item2, item3], 2, "consumables")
    assert shop.get_selected() == item3

# done b
def test_select_next():
    item1 = Item()
    item2 = Item()
    item3 = Item()
    shop = ShopListMenu([item1, item2, item3], 0, "consumables")
    shop.select_next()
    assert shop.selected_index == 1
    shop.select_next()
    assert shop.selected_index == 2
    shop.select_next()
    assert shop.selected_index == 2

# done b
def test_select_previous():
    item1 = Item()
    item2 = Item()
    item3 = Item()
    shop = ShopListMenu([item1, item2, item3], 2, "consumables")
    shop.select_previous()
    assert shop.selected_index == 1
    shop.select_previous()
    assert shop.selected_index == 0
    shop.select_previous()
    assert shop.selected_index == 0

# m
def test_store_attributes():
    item1 = Item()
    item2 = Item()
    item3 = Item()
    weapons = ShopListMenu([item1, item2, item3], 0, "weapons")
    armor = ShopListMenu([item1, item2, item3], 1, "armor") 
    consumables = ShopListMenu([item1, item2, item3], 2, "consumables") 

    store = Store(weapons, armor, consumables)

    assert store.weapons == weapons
    assert store.armor == armor
    assert store.consumables == consumables

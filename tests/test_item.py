"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item

discount = 0.85


@pytest.fixture
def item() -> Item:
    return Item("Смартфон", 1000, 2)


def test_item_initialized(item) -> None:
    assert item.name == "Смартфон"
    assert item.price == 1000
    assert item.quantity == 2


def test_calculate_total_price(item):
    assert item.price * item.quantity == 2000


def test_apply_discount(item):
    assert item.price * discount == 850


def test_instantiate_from_csv(item):
    item1 = Item.all[0]
    assert item1.name == 'Смартфон'
    item2 = Item.all[1]
    assert item2.name == 'Ноутбук'
    item2 = Item.all[1]
    assert item2.price == '1000'
    item3 = Item.all[2]
    assert item3.quantity == '5'


def test_string_to_number(item):
    assert Item.string_to_number("5") == 5
    assert Item.string_to_number("6.7") == 6
    assert Item.string_to_number("3.3") == 3


def test_repr(item):
    assert repr(item) == "Item('Смартфон', 1000, 2)"


def test_str(item):
    assert str(item) == 'Смартфон'

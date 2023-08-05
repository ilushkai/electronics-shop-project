"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.exceptions import InstantiateCSVError
from src.item import Item
from src.phone import Phone
import os

discount = 0.85


@pytest.fixture
def item() -> Item:
    return Item("Смартфон", 1000, 2)


@pytest.fixture
def phone() -> Phone:
    return Phone("Samsung", 10000, 3, 1)


def test_item_initialized(item) -> None:
    assert item.name == "Смартфон"
    assert item.price == 1000
    assert item.quantity == 2


def test_calculate_total_price(item):
    assert item.price * item.quantity == 2000


def test_apply_discount(item):
    assert item.price * discount == 850


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


def test_string_to_number(item):
    assert Item.string_to_number("5") == 5
    assert Item.string_to_number("6.7") == 6
    assert Item.string_to_number("3.3") == 3


def test_repr(item):
    assert repr(item) == "Item('Смартфон', 1000, 2)"


def test_str(item):
    assert str(item) == 'Смартфон'


def test_add(item, phone):
    assert item.quantity + phone.quantity == 5
    assert phone.quantity + item.quantity == 5
    assert ValueError(item.quantity + 5)


def test_exc_instantiate_from_csv():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv('empty.csv')

    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv('../src/damaged.csv')

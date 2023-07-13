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
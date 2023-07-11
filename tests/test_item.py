"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

price = 10000
quantity = 1
discount = 0.85
def test_calculate_price():
    assert price * quantity == 10000

def test_apply_discount():
    assert price * discount == 8500
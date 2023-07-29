import pytest
from src.phone import Phone

phone = Phone("Samsung", 10000, 3, 0)


def test_number_of_sim():
    assert ValueError(phone.number_of_sim)

from src.item import Item
import pytest
from src.keyboard import Keyboard

kb = Keyboard('Dark Project KD87A', 9600, 5)


def test_language():
    assert str(kb.language) == "EN"


def test_change_language():
    kb.change_lang()
    assert str(kb.language) == "RU"
    with pytest.raises(AttributeError):
        kb.language = 'FR'

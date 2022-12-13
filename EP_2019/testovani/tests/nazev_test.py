import pytest
import funkce.nazev


def test_secti():
    assert funkce.nazev.secti(5, 3) == 8

def test_bubble_sort():
    assert funkce.nazev.bubble_sort([2, 7, 9, 3]) == [2, 3, 7, 9]

def test_error():
    with pytest.raises(TypeError) as ex:
        funkce.nazev.error("text")
import pytest
from lib.sifra import ces_sifra, quick_sort

def test_sifry():
    assert ces_sifra("abc", 1) == "bcd".upper()


def test_neni_text():
    with pytest.raises(TypeError):
        assert ces_sifra(123, 2)

def test_sort():
    assert quick_sort([5, 1, 3, 2, 4]) == [1, 2, 3, 4, 5]

def test_neni_seznam_cisel():
    with pytest.raises(TypeError):
        assert quick_sort([1, 2, 3, "text"])

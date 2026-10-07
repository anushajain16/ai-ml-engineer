# Day 5 pytest example

from day_05_pytest.app.calculator import add, subtract


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(10, 4) == 6

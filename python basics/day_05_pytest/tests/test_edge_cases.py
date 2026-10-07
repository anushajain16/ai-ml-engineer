# Additional edge-case tests

from day_05_pytest.app.calculator import add


def test_add_zero_values():
    assert add(0, 0) == 0


def test_add_negative_values():
    assert add(-2, 5) == 3

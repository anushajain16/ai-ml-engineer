from day_02_oop.exercises import shapes
import pytest


@pytest.fixture
def rectangle():
    return shapes.Rectangle(4, 5)


@pytest.fixture
def another_rect():
    return shapes.Rectangle(3, 2)

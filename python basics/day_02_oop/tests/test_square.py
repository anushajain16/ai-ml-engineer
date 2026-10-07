import pytest
import day_02_oop.exercises.shapes as shapes

@pytest.mark.parametrize("side, area", [(5, 25), (10, 100), (0, 0)])
def test_square_area(side, area):
    square = shapes.Square(side)
    assert square.area() == area

@pytest.mark.parametrize("side, perimeter", [(5, 20), (10, 40), (0, 0)])
def test_square_perimeter(side, perimeter):
    square = shapes.Square(side)
    assert square.perimeter() == perimeter
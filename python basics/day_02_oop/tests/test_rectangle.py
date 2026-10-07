import day_02_oop.exercises.shapes as shapes
import pytest as pytest

class TestRectangle:

    def test_area(self, rectangle):
        assert rectangle.area() == 20   

    def test_perimeter(self, rectangle):
        assert rectangle.perimeter() == 18

    def test_equality(self, rectangle, another_rect):
        assert rectangle != another_rect
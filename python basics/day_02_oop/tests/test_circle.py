import math
import day_02_oop.exercises.shapes as shapes

class TestCircle:

    def setup_method(self, method):
        print(f"Setting up, {method}")
        self.circle = shapes.Circle(5)

    def teardown_method(self, method):
        print(f"Tearing down, {method}")

    def test_area(self):
        assert self.circle.area() == math.pi * 5 ** 2

    def test_perimeter(self):
        assert self.circle.perimeter() == 2 * math.pi * 5
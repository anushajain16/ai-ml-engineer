# Day 2 Exercise 3: OOP with shapes

class Shape:
    def area(self):
        return 0


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


r = Rectangle(5, 4)
print(r.area())

# Day 2 Exercise 2: Inheritance

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"


class Dog(Animal):
    def speak(self):
        return "Woof!"


d = Dog("Buddy")
print(d.name)
print(d.speak())

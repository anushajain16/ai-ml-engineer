# Day 2 Exercise 1: Class basics

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, I am {self.name} and I am {self.age} years old."


p1 = Person("Aisha", 21)
print(p1.greet())

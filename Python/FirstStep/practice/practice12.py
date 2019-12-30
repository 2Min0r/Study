# [practice12.py]
# coding: utf-8

# 12-1, 12-2, 12-3
class Shape():
    def __init__(self):
        pass
    
    def what_am_i(self):
        print("I am a {}".format(self.__class__.__name__))

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_perimeter(self):
        return self.length * self.width

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def change_size(self, num):
        self.side = self.side + num

    
    def calculate_perimeter(self):
        return self.side * self.side

shape = Shape()
shape.what_am_i()

rectangle = Rectangle(3, 4)
print(rectangle.calculate_perimeter())
rectangle.what_am_i()

square = Square(3)
print(square.calculate_perimeter())
square.change_size(-1)
print(square.side)
square.what_am_i()

# 12-4
class Horse():
    def __init__(self, name, weight, owner):
        self.name = name
        self.weight = weight
        self.owner = owner

class Rider():
    def __init__(self, name):
        self.name = name

john = Rider("John")
spike = Horse("Spike", 97, john)
print(spike.owner.name)
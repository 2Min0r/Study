# [practice11.py]
# coding: utf-8
import math

class Apple():
    def __init__(self, w, c, o, p):
        self.weight = w
        self.color = c
        self.origin = o
        self.price = p
    
class Circle():
    def __init__(self, r):
        self.radius = r
    
    def area(self):
        return self.radius * self.radius * math.pi
    
circle = Circle(10)
print("%0.2f" % circle.area())

class Triangle():
    def __init__(self, h, b):
        self.height  = h
        self.base = b
    
    def area(self):
        return self.height * self.base * 0.5

triangle = Triangle(10, 20)
print("%0.2f" % triangle.area())

class Hexagon():
    def __init__(self, s):
        self.side = s
    def calculate_perimeter(self):
        return self.side * 6
    def area(self):
        return (math.sqrt(3) * 3 * self.side ** 2) / 2

hexagon = Hexagon(9)
print("%0.2f" % hexagon.calculate_perimeter())
print("%0.2f" % hexagon.area())
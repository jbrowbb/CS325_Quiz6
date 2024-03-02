from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        area = math.pi * math.pow(self.radius,2)
        return area
    

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def get_area(self):
        area = math.pow(self.side,2)
        return area
    

class Rectangle(Shape):
    def __init__ (self, length, width):
        self.length = length
        self.width = width
    
    def get_area(self):
        area = self.length * self.width
        return area
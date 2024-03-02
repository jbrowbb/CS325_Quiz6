from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def set_width(self, width):
        self.radius = width / 2

    def set_height(self, height):
        self.radius = height / 2

    def get_area(self):
        return math.pi * math.pow(self.radius, 2)
    

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.height * self.width
    

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def get_area(self):
        return 0.5 * self.base * self.height
    

class Polygon(Shape):
    def __init__(self, sides, lengths):
        if len(sides) != len(lengths):
            raise ValueError("Sides and lengths must have the same nuber of elements")
        
        self.sides = sides
        self.lengths = lengths
    
    def get_area(self):
        center = [sum(x) / len(x) for x in zip(*self.lengths)]      # calculates the coordinate of the center of the polygon base
        triangles = []

        for i in range(len(self.sides)):
            next_i = (i + 1) % len(self.sides)
            triangles.append(Triangle(self.lengths[i], center[i]- center[next_i]))
        
        return sum(t.get_area() for t in triangles)     # interate though the sides of the polygon and creates triangles to approximate its area
#!/usr/bin/env python3
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """Abstract Base Class representing a generic shape."""
    
    @abstractmethod
    def area(self) -> float:
        pass
    
    @abstractmethod
    def perimeter(self) -> float:
        pass


class Circle(Shape):
    """Concrete implementation of a Circle."""
    
    def __init__(self, radius: float):
        self.radius = radius
        
    def area(self) -> float:
        return math.pi * (self.radius ** 2)
        
    def perimeter(self) -> float:
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Concrete implementation of a Rectangle."""
    
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
        
    def area(self) -> float:
        return self.width * self.height
        
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


def shape_info(shape) -> None:
    """
    Prints the area and perimeter of a shape.
    Relies on duck typing: as long as the object has area() and perimeter() 
    methods, it will function correctly regardless of explicit type checking.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")

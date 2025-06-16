import math

class Shape:
    """Base class for shapes."""
    
    def area(self):
        """To be implemented by subclasses."""
        raise NotImplementedError("Subclasses must implement this method")

class Rectangle(Shape):
    """Rectangle shape."""
    
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        """Calculate rectangle area."""
        return self.length * self.width

class Circle(Shape):
    """Circle shape."""
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        """Calculate circle area."""
        return math.pi * (self.radius ** 2)

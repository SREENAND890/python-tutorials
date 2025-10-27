from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        """Subclasses must implement this method"""
        pass

    @abstractmethod
    def perimeter(self):
        """Subclasses must implement this method"""
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

c = Circle(5)
print("Area:", c.area())
print("Perimeter:", c.perimeter())



"""shape_factory.py"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def calculate_area(self) -> float:
        """Calculate the area of the shape."""


class Circle(Shape):
    """A class representing a circle."""
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def calculate_area(self) -> float:
        """Calculate the area of a circle."""
        return math.pi * (self.radius ** 2)

class Square(Shape):
    """A class representing a square."""
    def __init__(self, side: float) -> None:
        self.side = side

    def calculate_area(self):
        return self.side ** 2

class Rectangle(Shape):
    """A class representing a rectangle."""
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def calculate_area(self) -> float:
        return self.height * self.width


class ShapeFactory:
    """A factory class for creating shapes."""

    @staticmethod
    def create_shape(shape_type: str, *args) -> Shape:
        """Create a shape based on the given type."""
        match shape_type.lower():
            case "circle":
                return Circle(*args)
            case "square":
                return Square(*args)
            case "rectangle":
                return Rectangle(*args)
            case _:
                raise ValueError("Invalid shape type")


# Testing the Factory
def main():
    # Create shapes using the factory
    shapes = [
        ShapeFactory.create_shape("circle", 5),
        ShapeFactory.create_shape("square", 4),
        ShapeFactory.create_shape("rectangle", 3, 7)
    ]

    # Calculate and display area for each shape
    for shape in shapes:
        print(f"Area of {shape.__class__.__name__}: {shape.calculate_area()}")


if __name__ == "__main__":
    main()

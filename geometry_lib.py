from math import pi, sqrt
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def is_right(self) -> bool:
        return False

class Circle(Shape):
    def __init__(self, radius: float):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    def area(self) -> float:
        return pi * self.radius ** 2

    def is_right(self) -> bool:
        return False

class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        sides = sorted((a, b, c))
        if sides[0] <= 0 or sides[0] + sides[1] <= sides[2]:
            raise ValueError("Invalid triangle sides")
        self.a, self.b, self.c = sides

    def area(self) -> float:
        s = (self.a + self.b + self.c) / 2
        return sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right(self) -> bool:
        # right triangle: a^2 + b^2 == c^2
        return abs(self.a**2 + self.b**2 - self.c**2) < 1e-9

# Factory to create shapes dynamically
class ShapeFactory:
    @staticmethod
    def create(shape_type: str, *args) -> Shape:
        shape_type = shape_type.lower()
        if shape_type == 'circle':
            return Circle(*args)
        elif shape_type == 'triangle':
            return Triangle(*args)
        else:
            raise ValueError(f"Unknown shape type: {shape_type}")

# Generic area computation without compile-time type knowledge
def compute_area(shape: Shape) -> float:
    return shape.area()

if __name__ == '__main__':
    import unittest

    class TestShapes(unittest.TestCase):
        def test_circle_area(self):
            c = Circle(1)
            self.assertAlmostEqual(c.area(), pi)

        def test_circle_negative(self):
            with self.assertRaises(ValueError):
                Circle(-1)

        def test_triangle_area(self):
            t = Triangle(3, 4, 5)
            self.assertAlmostEqual(t.area(), 6)

        def test_triangle_invalid(self):
            with self.assertRaises(ValueError):
                Triangle(1, 2, 3)

        def test_triangle_right(self):
            t = Triangle(3, 4, 5)
            self.assertTrue(t.is_right())

        def test_triangle_non_right(self):
            t = Triangle(4, 5, 6)
            self.assertFalse(t.is_right())

        def test_factory_circle(self):
            c = ShapeFactory.create('circle', 2)
            self.assertIsInstance(c, Circle)
            self.assertAlmostEqual(compute_area(c), pi * 4)

        def test_factory_triangle(self):
            t = ShapeFactory.create('triangle', 3, 4, 5)
            self.assertIsInstance(t, Triangle)
            self.assertTrue(t.is_right())

        def test_unknown_shape(self):
            with self.assertRaises(ValueError):
                ShapeFactory.create('square', 2)

    unittest.main()

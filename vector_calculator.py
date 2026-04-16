import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

    def unit_vector(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError('Cannot calculate unit vector for zero vector')
        return Vector(self.x / mag, self.y / mag)

    def component_decomposition(self):
        return self.x, self.y

# Example usage:
v = Vector(3, 4)
print('Magnitude:', v.magnitude())
print('Unit vector:', v.unit_vector().__dict__)
print('Component decomposition:', v.component_decomposition())

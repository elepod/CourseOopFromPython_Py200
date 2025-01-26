from typing import Union


class Vector:
    def __init__(self, x: Union[int, float] = 0, y: Union[int, float] = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y)

    def __truediv__(self, other):
        return Vector(self.x / other.x, self.y / other.y)


if __name__ == "__main__":
    v1 = Vector(2, 1)
    v2 = Vector(1, 2)
    print(v1 + v2)
    print(v1 - v2)
    print(v1 * v2)
    print(v1 / v2)




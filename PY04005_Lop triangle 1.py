import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, p):
        return math.sqrt((self.x - p.x) ** 2 + (self.y - p.y) ** 2)

class Triangle(Point):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


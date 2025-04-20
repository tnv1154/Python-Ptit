import math
import sys


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, p):
        return math.sqrt((self.x - p.x) ** 2 + (self.y - p.y) ** 2)

class Triangle:
    def __init__(self, a, b, c):
        self.ab = a.distance(b)
        self.bc = b.distance(c)
        self.ca = c.distance(a)
    def check(self):
        if self.ab <= 0 or self.bc <= 0 or self.ca <= 0:
            return False
        if max([self.ab, self.bc, self.ca]) * 2 >= self.ab + self.bc + self.ca:
            return False
        return True
    def dienTich(self):
        s = 0.25 * math.sqrt((self.ab + self.bc + self.ca) *
                             (-self.ca + self.ab + self.bc) *
                             (-self.ab + self.bc + self.ca) *
                             (-self.bc + self.ca + self.ab))
        return s

if __name__ == '__main__':
    i = 1
    inputs = sys.stdin.read().split()
    for _ in range(int(inputs[0])):
        Ax, Ay, Bx, By, Cx, Cy = map(float, inputs[i : i + 6])
        i += 6
        a = Point(Ax, Ay)
        b = Point(Bx, By)
        c = Point(Cx, Cy)
        tamGiac = Triangle(a, b, c)
        if tamGiac.check():
            print(f"{round(tamGiac.dienTich(), 2):.2f}")
        else:
            print("INVALID")
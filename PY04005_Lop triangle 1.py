import math
import sys


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, p):
        return math.sqrt(pow(self.x - p.x, 2) + pow(self.y - p.y,2))

class Triangle:
    def __init__(self, a, b, c):
        self.ab = a.distance(b)
        self.bc = b.distance(c)
        self.ac = c.distance(a)
    def check(self):
        if self.ab <= 0 or self.bc <= 0 or self.ac <= 0:
            return False
        if max([self.ab, self.bc, self.ac])*2 >= self.ab + self.bc + self.ac:
            return False
        return True
    def perimeter(self):
        return self.ab + self.bc + self.ac
if __name__ == '__main__':
    """Các tọa độ có thể nằm trên nhiều dòng và lẫn lộn giữa các test case sao cho tổng số tọa độ vẫn đủ theo số test case"""
    i = 1
    inputs = sys.stdin.read().split() # Đọc hết input đầu vào và lưu vào mảng
    for test in range(int(inputs[0])):
        Ax, Ay, Bx, By, Cx, Cy = map(float, inputs[i:i + 6])
        i += 6
        a = Point(Ax, Ay)
        b = Point(Bx, By)
        c = Point(Cx, Cy)
        tamGiac = Triangle(a, b, c)
        if tamGiac.check():
            print(f"{round(tamGiac.perimeter(), 3):.3f}")
        else:
            print("INVALID")



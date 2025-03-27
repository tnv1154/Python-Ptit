import math

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
        self.ac = c.distance(a)
    def check(self):
        # Kiểm tra điều kiện tồn tại tam giác:
        # 1. Tổng 2 cạnh phải lớn hơn cạnh còn lại
        # 2. Các cạnh phải khác 0
        if (self.ab <= 0 or self.bc <= 0 or self.ac <= 0):
            return False
        if (self.ab + self.bc <= self.ac or 
            self.bc + self.ac <= self.ab or 
            self.ab + self.ac <= self.bc):
            return False
        return True
    def perimeter(self):
        return self.ab + self.bc + self.ac
if __name__ == '__main__':
    for _ in range(int(input())):
        arr = list(map(float, input().split()))
        a = Point(arr[0], arr[1])
        b = Point(arr[2], arr[3])
        c = Point(arr[4], arr[5])
        tamGiac = Triangle(a, b, c)
        if tamGiac.check():
            print(f"{tamGiac.perimeter():.3f}")
        else:
            print("INVALID")



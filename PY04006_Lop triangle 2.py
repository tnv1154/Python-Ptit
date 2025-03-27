import math

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
    def area(self):
        dientich = 0.25 * math.sqrt((self.ab + self.bc + self.ac) *
                                    (-self.ac + self.ab + self.bc) *
                                    (-self.ab + self.bc + self.ac) *
                                    (-self.bc + self.ac + self.ab) )
        return dientich
if __name__ == '__main__':
    for _ in range(int(input())):
        arr = list(map(float, input().split()))
        a = Point(arr[0], arr[1])
        b = Point(arr[2], arr[3])
        c = Point(arr[4], arr[5])
        tamGiac = Triangle(a, b, c)
        if tamGiac.check():
            print(f"{round(tamGiac.area(), 2):.2f}")
        else:
            print("INVALID")

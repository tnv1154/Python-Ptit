
class Rectangle:
    def __init__(self, length, width, Color) -> None:
        self.length = length
        self.width = width
        self.Color = Color
    def perimeter(self):
        if self.length <= 0 or self.width <= 0:
            return "INVALID"
        return 2 * (self.length + self.width)
    def area(self):
        if self.length <= 0 or self.width <= 0:
            return "INVALID"
        return self.length * self.width
    def color(self):
        if self.length <= 0 or self.width <= 0:
            return "INVALID"
        return str(self.Color[0].upper() + self.Color[1:].lower())



if __name__ == '__main__':
    arr = input().split()
    r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
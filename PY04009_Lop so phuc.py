import sys


class SoPhuc:
    def __init__(self, thuc, ao):
        self.thuc = thuc
        self.ao = ao


if __name__ == '__main__':
    inputs = sys.stdin.read().split()
    i = 1
    for _ in range(int(inputs[0])):
        a, b, c, d = list(map(int, inputs[i:i+4]))
        i += 4
        x = SoPhuc(a, b)
        y = SoPhuc(c, d)

import sys


class SoPhuc:
    def __init__(self, thuc, ao):
        self.thuc = thuc
        self.ao = ao
    def cong(self, b):
        thuc = self.thuc + b.thuc
        ao = self.ao + b.ao
        return SoPhuc(thuc, ao)
    def nhan(self, b):
        thuc = (self.thuc * b.thuc) - (self.ao * b.ao)
        ao = (self.thuc * b.ao) + (b.thuc * self.ao)
        return SoPhuc(thuc, ao)

if __name__ == '__main__':
    inputs = sys.stdin.read().split()
    i = 1
    for _ in range(int(inputs[0])):
        a, b, c, d = list(map(int, inputs[i:i+4]))
        i += 4
        A = SoPhuc(a, b)
        B = SoPhuc(c, d)

import sys

class SoPhuc:
    def __init__(self, thuc, ao):
        self.thuc = thuc
        self.ao = ao
    def cong(self, b):
        thuc = self.thuc + b.thuc
        ao = self.ao + b.ao
        ans = SoPhuc(thuc, ao)
        return ans
    def nhan(self, b):
        thuc = (self.thuc * b.thuc) - (self.ao * b.ao)
        ao = (self.thuc * b.ao) + (b.thuc * self.ao)
        ans = SoPhuc(thuc, ao)
        return ans
    def __str__(self):
        native_ao = False
        if self.ao < 0:
            native_ao = True
            self.ao = abs(self.ao)
        if native_ao:
            return f"{self.thuc} - {self.ao}i"
        else:
            return f"{self.thuc} + {self.ao}i"


if __name__ == '__main__':
    inputs = sys.stdin.read().split()
    i = 1
    for _ in range(int(inputs[0])):
        a, b, c, d = list(map(int, inputs[i:i+4]))
        i += 4
        A = SoPhuc(a, b)
        B = SoPhuc(c, d)
        C = (A.cong(B)).nhan(A)
        tmp = A.cong(B)
        D = tmp.nhan(tmp)
        print(f"{C}, {D}")
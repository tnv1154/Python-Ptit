

class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau

    @staticmethod
    def gcd(a, b):
        if b == 0:
            return a
        return PhanSo.gcd(b, a % b)

    @staticmethod
    def lcm(a, b):
        return a / PhanSo.gcd(a, b) * b # (a * b) / gcd(a, b)

    def rutGon(self):
        ucln = PhanSo.gcd(self.tu, self.mau)
        self.tu /= ucln
        self.mau /= ucln

    def tong(self, b):
        self.rutGon()
        b.rutGon()
        bcnn = PhanSo.lcm(self.mau, b.mau)
        tmp1 = bcnn / self.mau
        tmp2 = bcnn / b.mau
        tu = self.tu * tmp1 + b.tu * tmp2
        mau = bcnn
        c = PhanSo(tu, mau)
        c.rutGon()
        return c

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    a = PhanSo(arr[0], arr[1])
    b = PhanSo(arr[2], arr[3])
    c = a.tong(b)
    print(f"{c.tu:.0f}/{c.mau:.0f}")
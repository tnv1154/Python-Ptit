

class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
    @staticmethod
    def gcd(a, b):
        if b == 0:
            return a
        else:
            return PhanSo.gcd(b, a % b)

    def rutGon(self):
        ucln = PhanSo.gcd(self.tu, self.mau)
        self.tu /= ucln
        self.mau /= ucln

if __name__ == '__main__':
    tu, mau = map(int, input().split())
    p = PhanSo(tu, mau)
    p.rutGon()
    print(f"{p.tu:.0f}/{p.mau:.0f}")

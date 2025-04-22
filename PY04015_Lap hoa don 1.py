
class HoaDon:
    def __init__(self, id, ten, old, new):
        self.id = "KH" + f"{id:02d}"
        self.ten = " ".join(ten.title().split())
        self.total = self.calc(old, new)

    def calc(self, old, new):
        soNuoc = new - old
        remain = soNuoc
        phuPhi = 0
        total = 0
        if remain <= 50:
            total = remain * 100
            phuPhi = 0.02
        elif remain <= 100:
            total = 50 * 100 + (remain - 50) * 150
            phuPhi = 0.03
        else:
            total = 50 * 100 + 50 * 150 + (remain - 100) * 200
            phuPhi = 0.05
        total += total * phuPhi
        return round(total, 0)


    def __str__(self):
        return f"{self.id} {self.ten} {self.total:.0f}"


def main():
    HoaDons = []
    for i in range(int(input())):
        ten = input().strip()
        old = int(input())
        new = int(input())
        hd = HoaDon(i + 1, ten, old, new)
        HoaDons.append(hd)
    HoaDons.sort(key=lambda x : -x.total)
    for hd in HoaDons:
        print(hd)

if __name__ == '__main__':
    main()
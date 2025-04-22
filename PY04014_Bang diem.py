
from decimal import Decimal


class HocSinh:
    def __init__(self, id, ten, tb):
        self.id = "HS" + f"{id:02d}"
        ten = ten.title()
        ans = ""
        words = ten.split()
        for word in words:
            ans += word + " "
        self.ten = ans.strip()
        self.tb = tb
        if self.tb >= 9:
            self.xepLoai = "XUAT SAC"
        elif self.tb >= 8:
            self.xepLoai = "GIOI"
        elif self.tb >= 7:
            self.xepLoai = "KHA"
        elif self.tb >= 5:
            self.xepLoai = "TB"
        else:
            self.xepLoai = "YEU"

    def __str__(self):
        return f"{self.id} {self.ten} {round(self.tb, 1):.1f} {self.xepLoai}"


def main():
    HocSinhs = []
    for i in range(int(input())):
        ten = input().strip()
        arr = list(map(Decimal, input().split()))
        tb = 0
        tb += arr[0] * 2 + arr[1] * 2
        for j in range(2, len(arr)):
            tb += arr[j]
        tb /= 10
        tb /= Decimal(1.2)
        hs = HocSinh(i + 1, ten, tb)
        HocSinhs.append(hs)
    HocSinhs.sort(key=lambda x: (-x.tb, x.id))
    for hs in HocSinhs:
        print(hs)

if __name__ == '__main__':
    main()

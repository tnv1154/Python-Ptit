
class GiaoVien:
    def __init__(self, id, ten, ma, tin, chuyenMon):
        self.ten = " ".join(ten.title().split())
        self.id = f"GV{id:02d}"
        if ma[0] == "A":
            self.mon = "TOAN"
        elif ma[0] == "B":
            self.mon = "LY"
        elif ma[0] == "C":
            self.mon = "HOA"

        uuTien = 0
        if ma[1] == "1":
            uuTien = 2.0
        elif ma[1] == "2":
            uuTien = 1.5
        elif ma[1] == "3":
            uuTien = 1.0
        else:
            uuTien = 0

        self.tong = tin * 2 + chuyenMon + uuTien
        if self.tong >= 18:
            self.ketQUa = "TRUNG TUYEN"
        else: self.ketQUa = "LOAI"

    def __str__(self):
        return f"{self.id} {self.ten} {self.mon} {round(self.tong, 1)} {self.ketQUa}"

def main():
    arr = []
    for i in range(int(input())):
        ten = input()
        ma = input()
        tin = float(input())
        chuyenMon = float(input())
        gv = GiaoVien(i + 1, ten, ma, tin, chuyenMon)
        arr.append(gv)

    arr.sort(key = lambda x : -x.tong)
    for gv in arr:
        print(gv)

if __name__ == "__main__":
    main()
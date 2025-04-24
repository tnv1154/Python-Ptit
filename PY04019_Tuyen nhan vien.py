

class NhanVien:
    def __init__(self, id, ten, lt, th):
        self.id = "TS0" + str(id)
        self.ten = " ".join(ten.title().split())
        self.tb = round((self.chuanHoaDiem(lt) + self.chuanHoaDiem(th)) / 2, 2)
        if self.tb > 9.5:
            self.xl = "XUAT SAC"
        elif self.tb >= 8:
            self.xl = "DAT"
        elif self.tb >= 5:
            self.xl = "CAN NHAC"
        else:
            self.xl = "TRUOT"

    def chuanHoaDiem(self, score):
        if score <= 10:
            return score
        else:
            return float(score/10)
    def __str__(self):
        return f"{self.id} {self.ten} {self.tb:.2f} {self.xl}"

def main():
    NhanViens = []
    for i in range(int(input())):
        NhanViens.append(NhanVien(i + 1, input().strip(), float(input()), float(input())))
    NhanViens.sort(key=lambda n: (-n.tb, n.id))
    for nv in NhanViens:
        print(nv)
if __name__ == "__main__":
    main()

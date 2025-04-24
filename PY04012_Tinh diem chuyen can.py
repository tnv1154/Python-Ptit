
class SinhVien:
    def __init__(self, msv, ten, lop):
        self.msv = msv
        self.ten = " ".join(ten.title().split())
        self.lop = lop
        self.chuyenCan = 10

    def TinhDiemChuyenCan(self, diemDanh):
        for c in diemDanh:
            if c == "v":
                self.chuyenCan -= 2
            elif c == "m":
                self.chuyenCan -= 1
        if self.chuyenCan < 0:
            self.chuyenCan = 0


    def __str__(self):
        return f"{self.msv} {self.ten} {self.lop} {self.chuyenCan} " + ("KDDK" if self.chuyenCan == 0 else "")

def main():
    SinhViens = []
    mp = {}
    cnt = 0
    n = int(input())
    for _ in range(n):
        msv = input().strip()
        ten = input().strip()
        lop = input().strip()
        SinhViens.append(SinhVien(msv, ten, lop))
        mp[msv] = cnt
        cnt += 1
    for i in range(n):
        msv, diemDanh = map(str, input().split())
        SinhViens[mp[msv]].TinhDiemChuyenCan(diemDanh)
    for sv in SinhViens:
        print(sv)

if __name__ == "__main__":
    main()

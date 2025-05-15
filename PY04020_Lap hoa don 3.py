
class HoaDon:
    def __init__(self, id, ten, sl, donGia, chietKhau):
        self.id = id
        self.ten = ten
        self.sl = sl
        self.donGia = donGia
        self.chietKhau = chietKhau
        self.tong = sl * donGia - chietKhau

    def __str__(self):
        return f"{self.id} {self.ten} {self.sl} {self.donGia} {self.chietKhau} {self.tong}"

def main():
    arr = []
    for i in range(int(input())):
        id = input()
        ten = input()
        sl = int(input())
        donGia = int(input())
        chietKhau = int(input())
        hd = HoaDon(id, ten, sl, donGia, chietKhau)
        arr.append(hd)
    arr.sort(key = lambda x : -x.tong)
    for hd in arr:
        print(hd)

if __name__ == '__main__':
    main()
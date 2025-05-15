
class SinhVien:
    def __init__(self, ten, c, t):
        self.ten = " ".join(ten.title().split())
        self.c = c
        self.t = t

    def __str__(self):
        return f"{self.ten} {self.c} {self.t}"

def main():
    arr = []
    for i in range(int(input())):
        ten = input()
        c, t = map(int, input().strip().split())
        sv = SinhVien(ten, c, t)
        arr.append(sv)
    arr.sort(key = lambda x : (-x.c, x.t, x.ten))
    for sv in arr:
        print(sv)


if __name__ == "__main__":
    main()

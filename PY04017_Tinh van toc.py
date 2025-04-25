from datetime import datetime


class Cua_ro:
    def __init__(self, ten, donVi, end, length = 120):
        self.ten = " ".join(ten.title().split())
        self.donVi = " ".join(donVi.title().split())
        id = ""
        for word in self.donVi.split():
            id += word[0]
        for word in self.ten.split():
            id += word[0]
        self.id = id
        start_time = datetime.strptime("6:00", "%H:%M")
        end_time = datetime.strptime(end, "%H:%M")
        time = (end_time - start_time).total_seconds() / 3600
        self.tocDo = length / time

    def __str__(self):
        return f"{self.id} {self.ten} {self.donVi} {round(self.tocDo, 0):.0f} Km/h"

def main():
    arr = []
    for i in range(int(input())):
        ten = input().strip()
        donVi = input().strip()
        end = input().strip()
        arr.append(Cua_ro(ten, donVi, end))
    arr.sort(key = lambda x : -x.tocDo)
    for x in arr:
        print(x)
if __name__ == "__main__":
    main()
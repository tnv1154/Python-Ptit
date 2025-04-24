from datetime import datetime


class HoaDon:
    def __init__(self, id, ten, room, start, end, dichVu):
        self.id = "KH" + f"{id:02d}"
        self.ten = " ".join(ten.title().split())
        self.room = room
        tang = room[0]
        if tang == "1": self.total = 25
        elif tang == "2": self.total = 34
        elif tang == "3": self.total = 50
        elif tang == "4": self.total = 80
        start_time = datetime.strptime(start, "%d/%m/%Y")
        end_time = datetime.strptime(end, "%d/%m/%Y")
        time = end_time - start_time
        time = time.total_seconds() // (60 * 60 * 24) + 1
        self.time = time
        self.total = self.time * self.total + dichVu

    def __str__(self):
        return f"{self.id} {self.ten} {self.room} {self.time:.0f} {self.total:.0f}"

def main():
    HoaDons = []
    for i in range(int(input())):
        ten = input().strip()
        room = input().strip()
        start = input().strip()
        end = input().strip()
        dichVu = int(input())
        HoaDons.append(HoaDon(i + 1, ten, room, start, end, dichVu))
    HoaDons.sort(key = lambda x : -x.total)
    for hd in HoaDons:
        print(hd)

if __name__ == '__main__':
    main()
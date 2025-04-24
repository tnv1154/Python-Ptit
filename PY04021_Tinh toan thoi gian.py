from datetime import datetime


class Player:
    def __init__(self, id, ten, start, end):
        self.id = id
        self.ten = " ".join(ten.title().split())
        self.time = self.TinhThoiGian(start, end)
    def TinhThoiGian(self, start, end):
        start_time = datetime.strptime(start, "%H:%M")
        end_time = datetime.strptime(end, "%H:%M")
        time = end_time - start_time
        time = time.total_seconds() / 3600
        return time
    def __str__(self):
        return f"{self.id} {self.ten} {int(self.time)} gio {(self.time - int(self.time)) * 60:.0f} phut"


def main():
    players = []
    for _ in range(int(input())):
        id = input()
        ten = input().strip()
        start = input().strip()
        end = input().strip()
        players.append(Player(id, ten, start, end))
    players.sort(key = lambda x : -x.time)
    for player in players:
        print(player)
if __name__ == '__main__':
    main()
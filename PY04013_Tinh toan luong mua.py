from datetime import datetime


class Tram:
    def __init__(self, id, ten, time, rain):
        self.id = "T" + f"{id:02d}"
        self.ten = ten
        self.time = time
        self.rain = rain

    def add(self, time, rain):
        self.time += time
        self.rain += rain

    def calc(self):
        self.tb = self.rain / self.time

    def __str__(self):
        return f"{self.id} {self.ten} {round(self.tb, 2):.2f}"

Trams = []
dic = {}
for i in range(int(input())):
    ten, start, end, rain = input().strip(), input().strip(), input().strip(), int(input().strip())
    time_start = datetime.strptime(start, "%H:%M")
    time_end = datetime.strptime(end, "%H:%M")
    time = time_end - time_start
    time = time.total_seconds() / 3600
    if ten not in dic:
        tram = Tram(i + 1, ten, time, rain)
        Trams.append(tram)
        dic[ten] = i
    else:
        Trams[dic[ten]].add(time, rain)
for tram in Trams:
    tram.calc()
    print(tram)







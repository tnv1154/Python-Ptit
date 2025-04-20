import math
from math import floor


class SinhVien:
    def __init__(self, msv, ten, mon1, mon2, mon3):
        self.msv = "SV" + f"{msv:02d}"
        ten = ten.lower()
        words = ten.split()
        fullName = ""
        for word in words:
            fullName += word[0].upper() + word[1:] + " "
        self.ten = fullName.strip()
        average = (mon1 * 3 + mon2 * 3 + mon3 * 2) / 8
        self.tb = math.ceil(average * 100) / 100
        self.rank = 0

    def __str__(self):
        return f"{self.msv} {self.ten} {self.tb:.2f} {self.rank}"

def cal_rank(SVlist):
    SVlist.sort(key = lambda x : (-x.tb, x.msv))
    rank = 1
    prev = -1
    for i in range(len(SVlist)):
        if i > 0 and SVlist[i].tb == SVlist[i - 1].tb:
            SVlist[i].rank = SVlist[i - 1].rank
        else:
            SVlist[i].rank = rank
        rank += 1
    return SVlist

n = int(input())
SVlist = []
for i in range(1, n + 1):
    SV = SinhVien(i, input().strip(), float(input()), float(input()), float(input()))
    SVlist.append(SV)
SVlist = cal_rank(SVlist)
for sv in SVlist:
    print(sv)




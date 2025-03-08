import math

n = int(input())
a = []
cnt = 0
for i in range(n):
    b = input()
    cnt += math.comb(b.count("C"), 2)
    a.append(b)
for colum in range(n):
    tmp = 0
    for row in a:
        if colum < len(row) and row[colum] == "C":
            tmp += 1
    cnt += math.comb(tmp, 2)
print(cnt)

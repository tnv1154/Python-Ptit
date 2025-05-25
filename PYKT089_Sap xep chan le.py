

n = int(input())
a = []
while len(a) < n:
    a.extend(list(map(int, input().split())))

chan = []
le = []
vitri = []#chẵn = 1, lẻ = 0

for i in range(n):
    if a[i] % 2 == 0:
        chan.append(a[i])
        vitri.append(1)
    else:
        le.append(a[i])
        vitri.append(0)

chan = sorted(chan)
le = sorted(le, reverse=True)

i, j = 0, 0
for x in range(n):
    if vitri[x] == 1:
        print(chan[i], end = " ")
        i += 1
    else:
        print(le[j], end = " ")
        j += 1
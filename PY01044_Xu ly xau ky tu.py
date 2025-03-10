
s1 = input().lower()
s2 = input().lower()
a1 = list(map(str, s1.split()))
a2 = list(map(str, s2.split()))
mp1 = {}
mp2 = {}
for i in a1:
    if i not in mp1:
        mp1[i] = 1
for i in a2:
    if i not in mp1:
        mp1[i] = 1
hop = sorted(list(mp1.keys()))
for i in a1:
    if i not in mp2:
        mp2[i] = 1
for i in a2:
    if i in mp2:
        mp2[i] += 1
giao = []
for x,y in mp2.items():
    if y != 1:
        giao.append(x)
giao = sorted(giao)
for i in hop:
    print(i, end=' ')
print()
for i in giao:
    print(i, end=' ')



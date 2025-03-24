
se = set()
s = input()
n = len(s)
l = []
if len(s) % 2 != 0:
    n -= 1
for i in range(0, n, 2):
    ss = s[i] + s[i + 1]
    tmp = int(ss)
    if tmp not in se:
        se.add(tmp)
        l.append(tmp)
for x in l:
    print(x, end=" ")

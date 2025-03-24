
se = set()
s = input()
n = len(s)
if len(s) % 2 != 0:
    n -= 1
for i in range(0, n, 2):
    ss = s[i] + s[i + 1]
    tmp = int(ss)
    se.add(tmp)
l = sorted(list(se))
for x in l:
    print(x, end=" ")

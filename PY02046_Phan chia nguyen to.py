import math
def nto(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

n = int(input())
a = list(map(int, input().split()))
se = set()
b = []
for x in a:
    if x not in se:
        se.add(x)
        b.append(x)
n = len(b)
pref = [0] * (n + 1)
for i in range(1, n+1):
    pref[i] = pref[i-1] + b[i-1]
ok = False
for i in range(n):
    left = pref[i+1]
    right = pref[n] - pref[i+2]
    if nto(left) and nto(right):
        ok = True
        print(i)
        break
if not ok:
    print("NOT FOUND")
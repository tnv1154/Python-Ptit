import math

def Nto(m):
    if m < 2:
        return False
    if m < 4:
        return True
    if m % 2 == 0 or m % 3 == 0:
        return False
    for j in range(5, int(math.sqrt(m) + 1), 6):
        if m % j == 0 or m % (j + 2) == 0:
            return False
    return True

n = int(input())
se = set()
a = list(map(int, input().split()))
b = []
for x in a:
    if x not in se:
        se.add(x)
        b.append(x)
n = len(b)
#Mảng cộng dồn
pref = [0] * (n + 1)
for i in range(1, n+1):
    pref[i] = pref[i-1] + b[i-1]
sum_left = 0
sum_right = 0
ok = False
for i in range(n):
    sum_left = pref[i]
    sum_right = pref[n] - pref[i]
    if Nto(sum_left) and Nto(sum_right):
        print(i-1)
        ok = True
        break

if not ok:
    print("NOT FOUND")

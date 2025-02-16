import math

n, k = list(map(int, input().split()))
l = pow(10, k-1)
r = pow(10, k) - 1
cnt = 0
for i in range(l, r + 1, 1):
    if math.gcd(n, i) == 1:
        print(i, end = "")
        cnt += 1
        if (cnt % 10 == 0):
            print()
        else: print(" ", end = "")
import math

def nto(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n) + 1), 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

for _ in range(int(input())):
    n = int(input())
    cnt = 0
    for i in range(1, n):
        if math.gcd(i, n) == 1:
            cnt += 1
    if (nto(cnt)):
        print("YES")
    else:
        print("NO")

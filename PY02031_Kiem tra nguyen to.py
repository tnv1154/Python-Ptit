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
            return  False
    return True

n, m = list(map(int, input().split()))
a = []
for i in range(n):
    b = list(map(int, input().split()))
    a.append(b)
for i in a:
    for j in i:
        if nto(j):
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()
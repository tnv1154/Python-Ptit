import math


def nto(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n) + 1), 1):
        if n % i == 0:
            return False
    return True

for x in range(int(input())):
    s = input()
    n = 0
    for i in s:
        n += int(i)
    if nto(n):
        print("YES")
    else:
        print("NO")
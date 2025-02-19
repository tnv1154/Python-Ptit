import math


def nto(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

for x in range(int(input())):
    s = input()
    n = int(s[-4:])
    if nto(n):
        print("YES")
    else:
        print("NO")
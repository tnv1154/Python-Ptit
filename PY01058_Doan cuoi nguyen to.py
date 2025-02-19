import math


def nto(n):
    if n < 2:
        return False
    if n < 4 :
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def check(s):
    n = int(s)
    return True if nto(n) else False

for x in range(int(input())):
    s = input()
    if check(s[-4:]):
        print("YES")
    else:
        print("NO")
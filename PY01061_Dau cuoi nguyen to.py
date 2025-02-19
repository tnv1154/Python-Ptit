import math

def nto(s):
    n = int(s)
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

for x in range(int(input())):
    s = input()
    if nto(s[:3]) and nto(s[-3:]):
        print("YES")
    else:
        print("NO")
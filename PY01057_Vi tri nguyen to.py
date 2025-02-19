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

def check(n):
    for i in range(0, len(n), 1):
        if nto(i) and n[i] not in ['2', '3', '5', '7']:
            return False
        elif not nto(i) and n[i] in ['2', '3', '5', '7']:
            return False
    return True


for x in range(int(input())):
    n = input()
    if check(n):
        print("YES")
    else:
        print("NO")

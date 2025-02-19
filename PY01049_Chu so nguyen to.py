import math

def nto(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def check(s):
    if not nto(int(len(s))):
        return False
    csnto = 0
    for i in s:
        if i in ['2','3','5','7']:
            csnto += 1
    if csnto > len(s) - csnto:
        return True
    else:
        return False

for x in range(int(input())):
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")
import math
from tabnanny import check


def nto(n):
    if n < 2:
        return False
    if n < 4 :
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n) + 1), 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def check(s):
    if not nto(len(s)):
        return False
    cnt = 0
    for i in s:
        if i in ['2', '3', '5', '7']:
            cnt += 1
    return cnt > len(s) - cnt

for x in range(int(input())):
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")
import math


def nto(s):
    if s < 2:
        return False
    if s < 4:
        return True
    if s % 2 == 0 or s % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(s) + 1), 6):
        if s % i == 0 or s % (i + 2) == 0:
            return False
    return True

def check(s):
    sum = 0
    for i in range(0, len(s), 1):
        if i % 2 == 0 and int(s[i]) % 2 == 1:
            return False
        elif i % 2 == 1 and int(s[i]) % 2 == 0:
            return False
        sum += int(s[i])
    if nto(sum):
        return True
    return False

for x in range(int(input())):
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")
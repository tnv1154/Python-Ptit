import math

csnt = [2, 3, 5, 7]
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

def check(s):
    sum = 0
    for i in s:
        if int(i) not in csnt:
            return False
        else:
            sum += int(i)
    if nto(sum):
        return True
    else:
        return False

for _ in range(int(input())):
    s = input()
    reversed_s = s[::-1]
    sum = 0
    if nto(int(s)) and nto(int(reversed_s)) and check(s):
        print("Yes")
    else:
        print("No")

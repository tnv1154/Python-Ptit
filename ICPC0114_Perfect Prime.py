import math

def nto(n):
    n = int(n)
    if n < 2: return False
    if n == 2: return True
    if n%2 == 0: return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def check(s):
    sum = 0
    reverse_s = s[::-1]
    for i in s:
        if not nto(i):
            return False
        else:
            sum += int(i)
    if nto(sum) and nto(reverse_s) and nto(s):
        return True
    return False

for i in range(int(input())):
    s = input()
    if check(s):
        print("Yes")
    else:
        print("No")

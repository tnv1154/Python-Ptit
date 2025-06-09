import math


def check(n):
    m = int(n)
    sum = 0
    for i in n:
        sum += math.factorial(int(i))
    if sum == m:
        return True
    else:
        return False

for _ in range(int(input())):
    n = input()
    if check(n):
        print("Yes")
    else:
        print("No")
import math

def check(n):
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


for i in range(int(input())):
    a, b = list(map(int, input().split()))
    gcd = math.gcd(a, b)
    sum = 0
    for i in str(gcd):
        sum += int(i)
    if check(sum):
        print("YES")
    else:
        print("NO")
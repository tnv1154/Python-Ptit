import math

def check(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n) + 1) ):
        if (n % i == 0):
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
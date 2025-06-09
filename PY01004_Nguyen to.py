import math

def is_prime(n):
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
    cnt = 1
    a = int(input())
    for j in range(2,a) :
        if math.gcd(j, a) == 1:
            cnt += 1
    if is_prime(cnt):
        print("YES")
    else:
        print("NO")

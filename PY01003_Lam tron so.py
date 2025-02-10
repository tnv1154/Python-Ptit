import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True

for i in range(int(input())):
    cnt = 0
    for j in range(int(input())):
        if math.gcd(i, j) == 1:
            cnt += 1
    if is_prime(cnt):
        print("YES")
    else:
        print("NO")

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
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

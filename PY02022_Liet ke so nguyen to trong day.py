import math

#Sang so nguyen to
prime = [1] * 1000001
def sieve():
    prime[0] = prime[1] = 0
    for i in range(2, 1001, 1):
        if prime[i]:
            for j in range(i * i, 1000001, i):
                prime[j] = 0
#kiem tra so nguyen to toi uu
"""
def nto(n):
    if n < 2:
        return False
    if n < 4 :
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True
"""
sieve()
n = int(input())
a = list(map(int, input().split()))
mp = {}
for i in a:
    if prime[i]:
        if i not in mp:
            mp[i] = 1
        else:
            mp[i] += 1
for x, y in mp.items():
    print(str(x) + " " + str(y))
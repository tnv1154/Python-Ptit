import math

prime = [1] * 10001
def sieve():
    prime[0] = prime[1] = 0
    for i in range(2, int(math.sqrt(10000) + 1)):
        if prime[i] == 1:
            for j in range(i * i, 10001, i):
                prime[j] = 0

sieve()
n = int(input())
a = list(map(int, input().split()))
nto = []
for i in range(10001):
    if prime[i] == 1:
        nto.append(i)
cnt = 0
_min = 0
for x in a:
    m = 10000
    for y in nto:
        m = min(m, abs(x - y))
    _min = max(_min, m)
print(_min)

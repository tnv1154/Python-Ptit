import math

prime = [0] * 1000002
a = [0]
def sieve():
    for i in range(0, 1000000, 1):
        prime[i] = 1
    prime[0] = prime[1] = 0
    for i in range(2, 1001, 1):
        if prime[i] == 1:
            for j in range(i*i, 1000001, i):
                prime[j] = 0
    #dua so nguyen to vao list
    for i in range(1, 1000001):
        if prime[i] == 1:
            a.append(i)

sieve()
n, x = list(map(int, input().split()))
for i in range(0, n + 1):
    print(str(x + a[i]), end=" ")
    x += a[i]

prime = [1] * 1000001
def sieve():
    prime[0] = prime[1] = 0
    for i in range(2, 1001, 1):
        if prime[i]:
            for j in range(i * i, 1000001, i):
                prime[j] = 0

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

prime = [1] * 1000001
def sieve():
    prime[0] = prime[1] = 0
    for i in range(2, 1001):
        if prime[i] == 1:
            for j in range(i * i, 1000001, i):
                prime[j] = 0

sieve()

for _ in range(int(input())):
    ans = []
    n = int(input())
    for i in range(11, n):
        reverse_i = int(str(i)[::-1])
        if prime[i] == 1 and reverse_i < n and prime[reverse_i] == 1 and i != reverse_i and reverse_i not in ans:
            ans.append(i)
            ans.append(reverse_i)
            print(i, reverse_i, end=" ")
    print()

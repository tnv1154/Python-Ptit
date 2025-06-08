
prime = [1] * 1000001
def sieve():
    prime[0] = prime[1] = 0
    for i in range(2, 1001, 1):
        if prime[i] == 1:
            for j in range(i * i, 1000001, i):
                prime[j] = 0

def check(i):
    if prime[i + 2] == 1 and prime[i + 6] == 1:
        return True
    elif prime[i + 4] == 1 and prime[i + 6] == 1:
        return True
    return False

sieve()
for t in range(int(input())):
    n = int(input())
    cnt = 0
    for i in range(2, n, 1):
        if prime[i] == 1:
            if i + 6 >= n:
                break
            if check(i):
                cnt += 1
                #print(i)
    print(cnt)

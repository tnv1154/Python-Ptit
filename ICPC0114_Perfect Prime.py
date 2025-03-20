import math

prime = [1] * 10000005
mp = {}
def sieve():
    prime[0] = prime[1] = 0
    for i in range(2, int(math.sqrt(10000001))):
        if prime[i] == 1:
            for j in range(i * i, 10000005, i):
                prime[j] = 0
    for i in range(2, 10000001):
        if prime[i] == 1:
            mp[i] = 1

def check(s):
    reverse_s = s[::-1]
    sum = 0
    if int(reverse_s) not in mp and int(s) not in mp:
        return False
    else:
        for i in s:
            if int(i) not in mp:
                return False
            else:
                sum += int(i)
        if sum not in mp:
            return False
    return True

sieve()
for i in range(int(input())):
    s = input()
    if check(s):
        print("Yes")
    else:
        print("No")

s = input()
n = len(s)
ok = [0] * (n + 2)
kq = [0] * (n + 2)

def display():
    for i in range(1, n + 1):
        print(s[kq[i] - 1], end = "")
    print()
#Quay lui
def backtrack(i):
    if i > n:
        display()
    for j in range(1, n + 1):
        if ok[j] == 0:
            ok[j] = 1
            kq[i] = j
            backtrack(i + 1)
            ok[j] = 0


backtrack(1)


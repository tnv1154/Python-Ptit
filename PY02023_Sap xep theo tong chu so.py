
def tongCs(n):
    s = sum(int(i) for i in str(n))
    return s

for x in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = sorted(a, key = lambda i : (tongCs(i), i))
    for i in b:
        print(i, end=" ")
    print()

def check(a, b, n):
    for i in range(n):
        if a[i] > b[i]:
            return False
    return True

for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a = sorted(a)
    b = sorted(b)
    if check(a, b, n):
        print("YES")
    else:
        print("NO")
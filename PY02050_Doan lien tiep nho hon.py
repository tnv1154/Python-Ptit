
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    d = [1] * n
    for i in range(1,n):
        cnt = 1
        if a[i] >= a[i-1]:
            d[i-1] += cnt
    print()
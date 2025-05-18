
for i in range(int(input())):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    for j in range(k, n):
        print(a[j], end = " ")
    for j in range(0, k):
        print(a[j], end = " ")
    print()
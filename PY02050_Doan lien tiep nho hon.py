
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print("1", end=" ")
    for i in range(1,n):
        cnt = 1
        for j in a[i-1:0:-1]:
            if j <= a[i]:
                cnt += 1
            else:
                break
        print(cnt, end=" ")
    print()
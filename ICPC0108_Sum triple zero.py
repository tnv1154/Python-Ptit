
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a = sorted(a)
    cnt = 0
    for i in range(len(a)-2):
        l = i + 1
        r = n - 1
        while l < r:
            s = a[i] + a[l] + a[r]
            if s == 0:
                cnt += 1
                l += 1
            elif s > 0:
                r -= 1
            else:
                l += 1
    print(cnt)
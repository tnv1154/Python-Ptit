
for i in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    se = set(arr)
    a = list(se)
    cnt = 0
    min_val = a[0]
    max_val = a[-1]
    for i in range(min_val, max_val+1):
        if i not in a:
            cnt += 1
    print(cnt)

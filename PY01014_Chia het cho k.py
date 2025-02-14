
a, k, n = list(map(int, input().split()))
cnt = 0
tmp = int(a / k)
if tmp * k < a:
    tmp += 1
i = 1
while i <= n:
    i = tmp * k
    if i <= n and i - a != 0:
        print(i - a, end = " ")
        cnt += 1
    tmp += 1
if cnt == 0 :
    print("-1")

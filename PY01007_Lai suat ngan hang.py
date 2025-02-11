

for i in range(int(input())):
    n, x, m = list(map(float, input().split()))
    cnt = 0
    while n < m :
        n += n * (x/100)
        cnt += 1
    print(cnt)
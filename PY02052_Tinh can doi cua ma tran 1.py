
a = []
n = int(input())
for i in range(n):
    b = list(map(int, input().split()))
    a.append(b)
k = int(input())
sumTren = 0
sumDuoi = 0
for i in range(n):
    for j in range(n):
        if j < i:
            sumDuoi += a[i][j]
        elif j > i:
            sumTren += a[i][j]

lech = abs(sumTren - sumDuoi)
if lech <= k:
    print("YES")
else :
    print("NO")
print(lech)
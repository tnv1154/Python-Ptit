
n = int(input())
a = []
for i in range(n):
    b = list(map(int, input().split()))
    a.append(b)
k = int(input())
sumTren = 0
sumDuoi = 0
for i in range(n):
    for j in range(n):
        if j < n -i - 1:
            sumTren += a[i][j]
        elif j > n - i - 1:
            sumDuoi += a[i][j]
sum = abs(sumTren - sumDuoi)
if sum <= k :
    print("YES")
else :
    print("NO")
print(sum)
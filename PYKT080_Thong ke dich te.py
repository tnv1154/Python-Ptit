
n, m = map(int, input().split())
a = []
for i in range(n):
    colum = list(map(int, input().split()))
    a.append(colum)
ans = 0
for row in range(n):
    for colum in range(m):
        if a[row][colum] == -1:
            for i in range(row - 1, row + 2):
                for j in range(colum - 1, colum + 2):
                    if 0 <= i < n and 0 <= j < m and a[i][j] != -1:
                        ans += a[i][j]
                        a[i][j] = 0

print(ans)
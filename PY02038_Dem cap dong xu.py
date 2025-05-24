
arr = []
n = int(input())
for i in range(n):
    arr.append(list(input().strip()))
cnt = 0
for i in range(n):
    row = 0
    col = 0
    for j in range(n):
        if arr[i][j] == "C":
            row += 1
        if arr[j][i] == "C":
            col += 1
    cnt += row * (row - 1) // 2
    cnt += col * (col - 1) // 2
print(cnt)

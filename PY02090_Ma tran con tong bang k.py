def solve():
    # Đọc input
    n, m, k = map(int, input().split())
    a = []
    for i in range(n):
        row = list(map(int, list(input())))
        a.append(row)
    
    # Tính ma trận tổng cộng dồn
    sum_matrix = [[0]*(m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            sum_matrix[i][j] = (sum_matrix[i-1][j] + 
                              sum_matrix[i][j-1] - 
                              sum_matrix[i-1][j-1] + 
                              a[i-1][j-1])
    
    # Đếm số ma trận con có tổng bằng k
    count = 0
    for i1 in range(n):
        for j1 in range(m):
            for i2 in range(i1, n):
                for j2 in range(j1, m):
                    # Tính tổng ma trận con từ (i1,j1) đến (i2,j2)
                    sub_sum = (sum_matrix[i2+1][j2+1] - 
                             sum_matrix[i2+1][j1] - 
                             sum_matrix[i1][j2+1] + 
                             sum_matrix[i1][j1])
                    if sub_sum == k:
                        count += 1
    return count

# Đọc số test case
t = int(input())
for _ in range(t):
    print(solve())
import sys


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def tranfer(self, n, m):
        t = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                t[i][j] = self.matrix[j][i]
        return Matrix(t)

    def nhan(self, t, n, m):
        ans = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                for k in range(m):
                    ans[i][j] += self.matrix[i][k] * t.matrix[k][j]
        return ans

if __name__ == '__main__':
    """Giống PY04007 nhưng input có thể nằm lung tung trên nhiều dòng"""
    inputs = sys.stdin.read().split()  # Đọc hết input đầu vào và lưu vào mảng
    index = 1  # Sử dụng biến để theo dõi vị trí trong inputs
    for _ in range(int(inputs[0])):
        n, m = map(int, inputs[index:index+2])
        index += 2
        matrix = []
        for _ in range(n):
            row = list(map(int, inputs[index:index + m]))
            index += m
            matrix.append(row)
        a = Matrix(matrix)
        t = a.tranfer(n, m)
        ans = a.nhan(t, n, m)
        for row in ans:
            for col in row:
                print(col, end=" ")
            print()

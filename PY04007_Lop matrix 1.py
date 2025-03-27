
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
    for _ in range(int(input())):
        n, m = list(map(int, input().split()))
        matrix = []
        for i in range(n):
            row = list(map(int, input().split()))
            matrix.append(row)
        a = Matrix(matrix)
        t = a.tranfer(n, m)
        ans = a.nhan(t, n, m)
        for row in ans:
            for col in row:
                print(col, end=" ")
            print()

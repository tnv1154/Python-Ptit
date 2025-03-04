n, k = map(int, input().split())
a = sorted(list(set(map(int, input().split()))))
n = len(a)
x = [0] * k


def display():
    print(' '.join(map(str, [a[i] for i in x])))

def Try(i, start):
    if i == k:
        display()
        return

    for j in range(start, n):
        x[i] = j
        Try(i + 1, j + 1)


Try(0, 0)
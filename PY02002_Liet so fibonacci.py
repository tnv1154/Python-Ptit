
f = list(range(95))
def fibo():
    f[1] = f[2] = 1
    for i in range(3, 94):
        f[i] = f[i-1] + f[i-2]

fibo()
for x in range(int(input())):
    a, b = list(map(int, input().split()))
    for i in range(a, b + 1):
        print(f[i], end = " ")
    print()
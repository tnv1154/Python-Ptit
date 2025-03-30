
def lamTron(n):
    if n >= 5:
        return 1
    else:
        return 0

for _ in range(int(input())):
    s = input()
    a = []
    for i in s:
        a.append(int(i))
    for i in range(len(a) - 1, 0, -1):
        a[i-1] += lamTron(a[i])
        a[i] = 0
    ans = ""
    for i in a:
        ans += str(i)
    print(ans)
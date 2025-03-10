
n, k = map(int, input().split())
a = list(map(str, input().split()))
mp = {}
for i in a:
    if i not in mp:
        mp[i] = 1
a = sorted(mp.keys())
n = len(a)
x = [0] * k
ans = []

def save():
    tmp = ""
    for i in range(k):
        if i == k - 1:
            tmp += a[x[i]]
        else:
            tmp += a[x[i]] + " "
    ans.append(tmp)

def Try(i, start):
    if i == k:
        save()
        return
    for j in range(start, n):
        x[i] = j
        Try(i + 1, j + 1)

Try(0, 0)
ans = sorted(ans)
for i in ans:
    print(i)
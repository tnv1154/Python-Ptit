
n = int(input())
a = list(map(int, input().split()))
a = sorted(a)
ok = False
for i in range(len(a) - 1):
    if a[i] + 1 != a[i+1]:
        print(a[i] + 1)
        ok = True
        break
if not ok:
    print(a[len(a) - 1] + 1)
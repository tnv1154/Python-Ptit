a = [2, 3, 5, 7]
n = int(input())
ans = set()
def ok(check):
    for i in check:
        if not i:
            return False
    return True

def Try(check, s):
    if len(s) >= 4 and ok(check) and s[-1]!="2":
        ans.add(int(s))
    if len(s) == n:
        return
    for i in range(4):
        tmp = [j for j in check]
        tmp[i] = True
        Try(tmp, s+str(a[i]))

Try([False, False, False, False], '')
ans = sorted(list(ans))
for i in ans:
    print(i)
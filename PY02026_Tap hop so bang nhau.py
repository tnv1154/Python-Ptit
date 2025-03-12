
def check(A, B):
    if len(A) != len(B):
        return False
    for i in range(len(A)):
        if A[i] != B[i]:
            return False
    return True

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
mpa = {}
mpb = {}
for i in a:
    if i not in mpa:
        mpa[i] = 1
for i in b:
    if i not in mpb:
        mpb[i] = 1
A = sorted(list(mpa.keys()))
B = sorted(list(mpb.keys()))
if check (A, B):
    print("YES")
else:
    print("NO")
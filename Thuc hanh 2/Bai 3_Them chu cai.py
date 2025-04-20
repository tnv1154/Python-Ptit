
#Chia va tri
def chiaVaTri(n, k):
    if n == 1:
        return "A"
    mid = 1 << (n - 1)
    if k == mid:
        return chr(ord("A") + n - 1)
    elif k < mid:
        return chiaVaTri(n - 1, k)
    else:
        return chiaVaTri(n - 1, k - mid)

for _ in range(int(input())):
    n, k = map(int, input().split())
    print(chiaVaTri(n, k))
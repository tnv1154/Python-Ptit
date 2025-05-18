

def cv(a, b, p, q):
    a = a.replace(p, q)
    b = b.replace(p, q)
    return int(a) + int(b)

for i in range(int(input())):
    p, q = list(map(str, input().strip().split()))
    s = input().split()
    if (len(s) > 1):
        x1, x2 = s[0], s[1]
    else:
        x1 = s[0]
        x2 = input()
    x = cv(x1, x2, p, q)
    y = cv(x1, x2, q, p)
    print(min(x, y), max(x, y))

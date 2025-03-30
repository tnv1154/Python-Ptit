
def tinhTong(a):
    x = y = z = -100000000
    if len(a) < 3:
        return 0
    for i in a:
        if i > x:
            z = y
            y = x
            x = i
        elif i > y:
            z = y
            y = i
        elif i > z:
            z = i
    return x + y + z

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    se = set(a)
    a = list(se)
    print(a)
    print(tinhTong(a))

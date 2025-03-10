
while True:
    n = int(input())
    if n == 0:
        break
    a = []
    for i in range(n):
        x = int(input())
        a.append(x)
    _max = max(a)
    _min = min(a)
    if _max == _min:
        print("BANG NHAU")
    else:
        print(str(_min) + " " + str(_max))
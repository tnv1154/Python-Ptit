
for x in range(int(input())):
    inp = int(input())
    ans = 0.0
    if inp % 2 == 0:
        for i in range(2, inp + 1, 2):
            ans += 1.0 / i
    else:
        for i in range(1, inp + 1, 2):
            ans += 1.0 / i
    print("{:.6f}".format(ans))
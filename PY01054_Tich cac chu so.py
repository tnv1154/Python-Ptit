
for x in range(int(input())):
    s = input()
    n = 1
    for i in s:
        if int(i) != 0:
            n *= int(i)
    print(n)
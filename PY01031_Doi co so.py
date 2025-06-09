
for x in range(int(input())):
    n, b = map(int, input().split())
    remainder = n
    sb = ""
    while remainder > 0:
        m = remainder % b
        if m >= 10:
            sb = sb + chr(m + ord("A") - 10)
        else:
            sb = sb + str(m)
        remainder = int(remainder / b)
    sb = "".join(reversed(sb))
    print(sb)

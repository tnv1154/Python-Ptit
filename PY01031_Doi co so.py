
for x in range(int(input())):
    n, b = map(int, input().split())
    remainder = n
    sb = ""
    while remainder > 0:
        if b > 10:
            m = remainder % b
            if m >= 10:
                sb = sb + chr(int(m) + ord("A") - 10)
            else:
                sb = sb + str(m)
        else:
            sb = sb + str(remainder % b)
        remainder = int(remainder / b)
    sb = "".join(reversed(sb))
    print(sb)

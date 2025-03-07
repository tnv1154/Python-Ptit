
def doiCs10(s):
    return int(s, 2)  # Chuyển trực tiếp chuỗi nhị phân sang thập phân


def doiCs(s, b):
    cs10 = doiCs10(s)
    if b != 4 and b != 8 and b != 16:
        return ""
    sb = ""
    m = 0
    remainder = cs10
    while (remainder > 0):
        if (b > 10):
            m = remainder % b
            if (m >= 10):
                sb = sb + str(chr(55 + m))
            else:
                sb = sb + str(m)
        else:
            sb = sb + str(remainder % b)
        remainder = int(remainder / b)
    return "".join(reversed(sb))


for x in range(int(input())):
    b = int(input())
    s = input()
    if b == 2:
        print(s)
    else:
        print(str(doiCs(s, b)))


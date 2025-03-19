def doiCs10(s):
    return int(s, 2)

def doiCs(s, b):
    cs10 = doiCs10(s)
    if b == 10:
        return cs10
    if b != 4 and b != 8 and b != 16:
        return ""
    if cs10 == 0:
        return "0"
    sb = ""
    while cs10 > 0:
        m = cs10 % b
        if m >= 10:
            sb = chr(55 + m) + sb
        else:
            sb = str(m) + sb
        cs10 //= b
    return sb

for x in range(int(input())):
    b = int(input())
    s = input()
    if b == 2:
        print(s)
    else:
        print(doiCs(s, b))

def doiCs(n, b):
    remainder = n
    sb = ""
    m = 0
    while remainder > 0 :
        if b > 10:
            m = remainder % b
            if m >= 10:
                sb = sb + str(chr(55 + m))
            else:
                sb = sb + str(m)
        else:
            sb = sb + str(remainder % b)
        remainder = int(remainder / b)
    return "".join(reversed(sb))

for i in range(int(input())):
    n , b = list(map(int, input().split()))
    print(doiCs(n, b))
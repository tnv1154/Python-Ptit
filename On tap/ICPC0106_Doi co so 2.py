
def chuyen_doi(s, b):
    a = int(s, 2)  # chuyen nhi phan sang thap phan
    if b == 10:
        return a
    if b != 4 and b != 8 and b != 16:
        return ""
    if a == 0:
        return "0"
    sb = ""
    while a > 0:
        m = a % b
        if m >= 10:
            sb = chr(55 + m) + sb
        else:
            sb = str(m) + sb
        a = a // b
    return sb

for _ in range(int(input())):
    b = int(input())
    s = input()
    if b == 2:
        print(s)
    else:
        print(chuyen_doi(s, b))
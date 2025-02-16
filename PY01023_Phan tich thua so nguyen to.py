
def phanTich(s):
    thisDict = dict()
    i = 2
    cnt = 0
    n = int(s)
    while n > 1:
        if (n % i == 0):
            cnt += 1
            n = int(n / i)
            if cnt != 0 :
                thisDict.update({i : cnt})
        else:
            i += 1
            cnt = 0
    if n > 1:
        thisDict.update({n : 1})
    return thisDict

for x in range(int(input())):
    s = input()
    thisDict = phanTich(s)
    print("1", end = "")
    for x, y in thisDict.items():
        print(" * " + str(x) + "^" + str(y), end = "")
    print()


for x in range(int(input())):
    s = input()
    sum = 0
    tich = 1
    ok = False
    for i in range(len(s)):
        if i % 2 == 0:
            sum += int(s[i])
        else:
            if int(s[i]) > 0:
                ok = True
                tich *= int(s[i])
    if ok:
        print(str(sum) + " " + str(tich))
    else:
        print(str(sum) + " 0")
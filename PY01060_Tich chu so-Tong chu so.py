
for x in range(int(input())):
    s = input()
    sum = 0
    tich = 1
    ok = False
    for i in range(len(s)):
        if i & 1 == 0:
            if int(s[i]) > 0:
              ok = True
              tich *= int(s[i])
        else:
            sum += int(s[i])
    if ok:
        print(str(tich) +" "+ str(sum))
    else:
        print("0 "+str(sum))
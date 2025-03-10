
def check(s):
    for i in s:
        if i != "6" and i != "8":
            return False
    cnt8 = 0
    for i in s:
        if i == "8":
            cnt8 += 1
        elif i == "6":
            cnt8 = 0
        if cnt8 == 3:
            return False
    return True


s = input()
if check(s):
    print("YES")
else:
    print("NO")

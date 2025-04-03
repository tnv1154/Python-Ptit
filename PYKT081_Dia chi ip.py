
def check(s):
    cnt = 0
    for x in s:
        if x.isdigit() or x == ".":
            if x == ".":
                cnt += 1
        else:
            return False
    if cnt != 3:
        return False
    a = s.split(".")
    for x in a:
        if len(x) == 0 :
            return False
        tmp = int(x)
        if tmp > 255 or tmp < 0:
            return False
    return True

for _ in range(int(input())):
    s = input().strip()
    if check(s):
        print("YES")
    else:
        print("NO")



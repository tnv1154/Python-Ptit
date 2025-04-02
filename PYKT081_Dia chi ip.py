
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


for _ in range(int(input())):
    s = input().strip()
    if check(s):
        print("YES")
    else:
        print("NO")

for x in range(int(input())):
    s = input() + "#"
    cnt = 1
    for i in range(0, len(s) - 1, 1):
        if s[i] == s[i + 1]:
            cnt += 1
        else :
            print(str(cnt) + s[i], end = "")
            cnt = 1
    print()
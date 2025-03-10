
for x in range(int(input())):
    s = input()
    ans = ""
    for i in range(1, len(s), -1):
        if s[i] < s[i-1]:
           ans = s[:i-1] + s[i] + s[i-1]
        if len(str(int(ans))) != len(s):
            ans = ""
    if ans == "":
        print("-1")
    else:
        print(ans)
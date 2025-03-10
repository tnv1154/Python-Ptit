
def mind(s, i):
    tmp = i
    for j in range(i+1, len(s)):
        if int(s[j]) < int(s[i]):
            if tmp == i:
                tmp = j
            elif s[tmp] < s[j]:
                tmp = j
    if s[tmp] < s[i]:
        return tmp
    return -1

for x in range(int(input())):
    s = input()
    n = len(s)
    ans = ""
    for i in range(n-1, -1, -1):
        idx = mind(s, i)
        if idx > -1:
            ans = s[:i] + s[idx] + s[i+1:idx] + s[i] + s[idx+1:]
            break

    if ans != "" and ans != s and ans[0] != "0":
        print(ans)
    else:
        print("-1")
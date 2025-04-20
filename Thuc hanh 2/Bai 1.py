
def maHoa(s):
    ans = ""
    i = 0
    while i < len(s):
        cnt = 1
        while i < len(s) - 1 and s[i] == s[i + 1]:
            cnt += 1
            i += 1
        ans += str(cnt) + s[i]
        i += 1
    print(ans)

t = int(input())
for x in range(t):
    s = input()
    maHoa(s)
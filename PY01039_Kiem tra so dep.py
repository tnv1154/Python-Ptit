
def check(s):
    if s[0] == s[1]:
        return False
    for i in range(2, len(s)):
        # s[i & 1] : nếu i chẵn = 0, i lẻ = 1
        if s[i] != s[i & 1]:
            return False
    return True

for x in range(int(input())):
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")
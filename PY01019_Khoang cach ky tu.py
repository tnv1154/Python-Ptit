def check(s):
    reverse_s = s[::-1]
    for i in range(len(s)):
        if abs(ord(s[i]) - ord(s[i-1])) != abs(ord(reverse_s[i]) - ord(reverse_s[i-1])):
            return False
    return True

for x in range(int(input())):
    s = input()
    if check(s) :
        print("YES")
    else:
        print("NO")
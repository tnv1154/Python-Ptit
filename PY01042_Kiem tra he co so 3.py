
for x in range(int(input())):
    s = input()
    for i in range(len(s)):
        if (s[i] not in ['0', '1', '2']):
            print("NO")
            break
        elif i == len(s) - 1:
            print("YES")
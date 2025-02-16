
def check(s):
    sum = 0
    for i in range(0, len(s) - 1, 1):
        sum += int(s[i])
        if abs(int(s[i]) - int(s[i+1])) != 2:
            return False
    sum += int(s[len(s) - 1])
    if sum % 10 == 0:
        return True
    else:
        return False

for x in range(int(input())):
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")
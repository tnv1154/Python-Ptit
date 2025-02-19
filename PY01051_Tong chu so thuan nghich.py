
def check(s):
    if len(s) <= 1:
        return False
    reverse_s = s[::-1]
    if s != reverse_s:
        return False
    return True

for x in range(int(input())):
    s = input()
    n = 0
    for i in s:
        n += int(i)
    if check(str(n)):
        print("YES")
    else:
        print("NO")

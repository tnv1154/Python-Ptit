
def find_idx(s):
    for i in range(0, len(s) - 1):
        if s[i] >= s[i+1]:
            return i
    return len(s) - 1

def check(s):
    if len(s) < 3:
        return False
    idx = find_idx(s)
    if idx != len(s) - 1:
        for i in range(idx, len(s) - 1):
            if s[i] <= s[i+1]:
                return False
    else :
        return False
    return True

for x in range(int(input())):
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")

def check(s1, s2):
    for i in s1:
        if s1.count(i) != s2.count(i):
            return False
    return True

for i in range(int(input())):
    s1 = input()
    s2 = input()
    if check(s1, s2):
        print("Test " + str(i+1) + ": YES")
    else:
        print("Test " + str(i+1) + ": NO")
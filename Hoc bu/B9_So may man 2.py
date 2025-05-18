
def check(n):
    for i in n:
        if i != "4" and i != "7":
            return False
    return True

for i in range(int(input())):
    a = input()
    if check(a):
        print("YES")
    else:
        print("NO")
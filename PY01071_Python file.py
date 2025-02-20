
def check(s):
    if len(s) < 1 or len(s) > 128:
        return False
    a = s.split(".")
    if len(a) != 2:
        return False
    if a[1].lower() != "py":
        return False
    for i in a[0]:
        if not ( ('a' <= i <= 'z') or ('A' <= i <'Z') or i == '.' or i == '_' ):
            return False
    return True

s = input()
if check(s):
    print("yes")
else:
    print("no")

s = input()
f = [0] * 15

def Try(ss):
    if len(ss) == len(s):
        print(ss)
        return
    for i in range(len(s)):
        if f[i] == 0:
            f[i] = 1
            Try(ss + s[i])
            f[i] = 0

Try("")

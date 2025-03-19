
s = input()
sum = 0
while int(s) >= 10:
    n = len(s) // 2
    sum = int(s[0:n]) + int(s[n:])
    print(sum)
    s = str(sum)



p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while True :
    str = input()
    if str[0] == "0":
        break
    k, s = str.split()
    k = int(k)
    tmp = ""
    for i in range(len(s)):
        tmp += p[(p.find(s[i]) + k) % 28]
    print(tmp[::-1])

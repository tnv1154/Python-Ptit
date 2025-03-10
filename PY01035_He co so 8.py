
s = input()
ans = ""
remaider = len(s) % 3
if remaider != 0:
    s = "0" * (3 - remaider) + s

for i in range(0, len(s), 3):
    ss = s[i:i+3]
    sum = 0
    for i in range(0, len(ss), 1):
        if ss[i] == "1":
            sum += (2 ** (len(ss) - i - 1))
    ans = ans + str(sum)
print(ans)
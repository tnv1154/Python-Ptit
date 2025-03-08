
s = input()
remainder = len(s) % 3
if remainder != 0:
    s = "0" * (3 - remainder) + s
ans = ""
for i in range(0, len(s), 3):
    ss = s[i:i+3]
    x = 0
    for j in range(0, len(ss), 1):
        x = x + int(ss[j]) * (2 ** (len(ss)-j-1))
    ans = str(x) + ans
print("".join(reversed(ans)))

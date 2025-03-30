
s = input()
hoa = thuong = 0
for i in s:
    if i.islower():
        thuong += 1
hoa = len(s) - thuong
if hoa > thuong:
    print(s.upper())
else:
    print(s.lower())
s = input()
thuong = 0
for i in s:
    if i.islower():
        thuong += 1
if thuong >= len(s) - thuong:
    print(s.lower())
else:
    print(s.upper())


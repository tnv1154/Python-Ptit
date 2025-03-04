import re

for i in range(int(input())):
    s = input()
    a = list(map(int, re.findall(r"\d+",s)))
    print(max(a))
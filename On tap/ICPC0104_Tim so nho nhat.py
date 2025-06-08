import re

for _ in range(int(input())):
    s = input()
    a = list(map(int, re.findall(r'\d+', s)))
    print(min(a))
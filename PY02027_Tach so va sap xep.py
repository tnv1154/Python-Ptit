import re

ans = []
for _ in range(int(input())):
    s = input()
    ss = re.findall(r'\d+', s)
    for j in ss:
        ans.append(int(j))
ans.sort()
for i in ans:
    print(i)

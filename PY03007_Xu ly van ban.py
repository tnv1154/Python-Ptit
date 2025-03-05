import re
f = []
while True:
    try:
        line = input().strip()
        if line:
            f.append(line)
    except : break

for i in f:
    i = i.lower().strip()
    line = re.split(r'[!.?]+', i)
    a = []
    for i in line:
        b = i.strip().split()
        if len(b) != 0: # xử lý câu có ít nhất 1 từ
            a.append(b)
    for l in a:
        print(l[0][0].upper() + l[0][1:].lower(), end = " ")
        for i in range(1, len(l)):
            if i != len(l) - 1:
                print(l[i], end = " ")
            else:
                print(l[i], end = "")
        print()




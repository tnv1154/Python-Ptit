

se = set()
with open("File/CONTACT.in") as f:
    for line in f:
        s = line.strip()
        s = s.lower()
        se.add(s)
    a = list(se)
    a.sort()

for x in a:
    print(x)

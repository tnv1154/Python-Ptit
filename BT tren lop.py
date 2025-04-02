
a = []
with open("File/CONTACT.in") as f:
    for line in f:
        print(line)

with open("File/CONTACT.in") as f:
    lines = f.readlines()
    for line in lines:
        print(line.rstrip())
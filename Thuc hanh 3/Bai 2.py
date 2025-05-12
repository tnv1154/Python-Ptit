import re

INT_MIN = -2**31
INT_MAX = 2**31-1
with open("DATA.in", "r") as file:
    lines = file.readlines()

words = []
for line in lines:
    tmp = line.strip().split()
    for word in tmp:
        if re.fullmatch(r"-?\d+", word):
            try:
                num = int(word)
                if INT_MIN <= num <= INT_MAX:
                    continue
            except ValueError:
                pass
        words.append(word)

words.sort()
print(" ".join(words))
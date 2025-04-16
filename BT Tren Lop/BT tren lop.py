
a = []
with open("../File/CONTACT.in") as f:
    for line in f:
        a.extend(line.strip().split())
mp = {}
for x in a:
    if x in mp:
        mp[x] += 1
    else:
        mp[x] = 1
for x, y in mp.items():
    print(x, y)

# In ra 10 từ có số lần xuất hiện lớn nhất
print("\n10 từ xuất hiện nhiều nhất:")
sorted_words = sorted(mp.items(), key=lambda item: item[1], reverse=True)
for word, count in sorted_words[:10]:
    print(f" {word}: {count}")
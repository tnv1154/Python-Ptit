
n = int(input())
mp = {}
for i in range(n):
    s = input().strip()
    if s not in mp.keys():
        mp[s] = 1
print(len(mp.keys()))
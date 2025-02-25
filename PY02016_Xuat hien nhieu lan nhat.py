
for x in range(int(input())):
    n = int(input())
    mp = {}
    a = list(map(int, input().split()))
    for i in a:
        if mp.get(i):
            mp[i] += 1
        else :
            mp[i] = 1
    maxCnt = max(mp.values())
    minKey = 10e9
    if maxCnt > n / 2:
        for a, b in mp.items():
            if b == maxCnt and a < minKey:
                minKey = a
        print(minKey)
    else :
        print("NO")
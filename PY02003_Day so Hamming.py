
a = []
mp = {}

for i in range(60):
    for j in range(38):
        for z in range(26):
            num = (2 ** i) * (3 ** j) * (5 ** z)
            if num not in mp:
                mp[num] = 1
                a.append(num)

a.sort()

def binarySearch(l, r, x):
    while(l <= r):
        mid = (l + r) // 2;
        if x == a[mid]:
            return mid + 1
        if a[mid] > x:
            r = mid - 1
        else:
            l = mid + 1
    return -1

for x in range(int(input())):
    x = int(input())
    idx = binarySearch(0, len(a), x)
    if idx == -1:
        print("Not in sequence")
    else:
        print(idx)

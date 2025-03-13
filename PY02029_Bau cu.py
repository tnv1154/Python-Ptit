
n, m = map(int, input().split())
a = list(map(int, input().split()))

mp = {}
for i in a:
    if i not in mp:
        mp[i] = 1
    else:
        mp[i] += 1
#Sắp xếp mảng giảm dần value, và tăng dần theo key nếu value = nhau
a = sorted(mp, key=lambda x: (-mp.get(x), x))
#lấy tần suất lớn nhất
_max = mp[a[0]]
while len(a) > 0 and mp[a[0]] == _max:
    a.pop(0)
if len(a) == 0:
    print("NONE")
else:
    print(a[0])
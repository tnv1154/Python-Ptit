
n = int(input())
a = list(map(int, input().split()))
idx = -1
_min = 10000000
for i in range(n):
    sum = 0
    for j in range(n):
        sum += abs(a[i] - a[j])
    if sum < _min:
        idx = i
        _min = sum
print(_min, a[idx])
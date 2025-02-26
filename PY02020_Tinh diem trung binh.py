
n = int(input())
diem = list(map(float, input().split()))
minVal = min(diem)
maxVal = max(diem)
sum = 0
cnt = 0
for i in diem:
    if i != minVal and i != maxVal:
        sum += i
        cnt += 1
tb = sum / cnt
print("{:.2f}".format(tb))

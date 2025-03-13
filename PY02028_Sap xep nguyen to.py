import math

def nto(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n) + 1), 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

n = int(input())
a = list(map(int, input().split()))
#Mảng đánh dấu vị trí số nguyên tố
b = []
#Mảng lưu các số nguyên tố
c = []
for i in range(n):
    if nto(a[i]):
        b.append(1)
        c.append(a[i])
    else:
        b.append(0)
c = sorted(c)
j = 0
#Mảng kết quả
ans = []
for i in range(len(a)):
    if b[i] == 1:
        ans.append(c[j])
        j += 1
    else:
        ans.append(a[i])
for i in ans:
    print(i, end=" ")
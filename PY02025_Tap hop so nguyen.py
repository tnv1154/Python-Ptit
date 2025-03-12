
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
mpa = {}
mpb = {}
#Tạo dictionary chứa các giá trị khác nhau trong a,b
for i in a:
    if i not in mpa:
        mpa[i] = 1
for i in b:
    if i not in mpb:
        mpb[i] = 1
#Chuyển dictionary thành list
A = sorted(list(mpa.keys()))
B = sorted(list(mpb.keys()))
#Giao 2 mảng
for i in A:
    if i in B:
        print(i, end = " ")
print()
#Hiệu mảng A - B, thuộc A nhưng ko thuộc B
for i in A:
    if i not in B:
        print(i, end = " ")
print()
#Hiệu mảng B - A
for i in B:
    if i not in A:
        print(i, end = " ")

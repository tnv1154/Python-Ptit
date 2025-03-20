
giaiThua = []
def tinhGiaiThua():
    ans = 1
    giaiThua.append(ans)
    for i in range(1, 11):
        ans = ans * i
        giaiThua.append(ans)

tinhGiaiThua()
for i in range(int(input())):
    s = input()
    sum = 0
    for j in s:
        sum += giaiThua[int(j)]
    if sum == int(s):
        print("Yes")
    else:
        print("No")
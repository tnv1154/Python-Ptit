
giaiThua = [1 for i in range(10)]
def tinhGiaiThua():
    for i in range(1, 10):
        giaiThua[i] = i * giaiThua[i-1]

tinhGiaiThua()
for _ in range(int(input())):
    s = input()
    n = int(s)
    s = str(n)
    sum = 0
    for i in s:
        sum += giaiThua[int(i)]
    if sum == n:
        print("Yes")
    else:
        print("No")
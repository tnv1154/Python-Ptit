
def tichCs(n):
    tich = 1
    for i in str(n):
        tich *= int(i)
    return tich

for x in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = sorted(a, key = lambda i : (tichCs(i), i))
    for i in b:
        print(i, end=" ")
    print()
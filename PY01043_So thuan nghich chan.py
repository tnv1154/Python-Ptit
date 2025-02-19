
list = []

def check(n):
    if len(str(n)) % 2 != 0:
        return False
    s = str(n)
    reverse_s = s[::-1]
    if s != reverse_s:
        return False
    for i in s:
        if int(i) % 2 != 0:
            return False
    return True

def solve(start, end):
    for i in range(start, end, 2):
        if check(i):
            list.append(i)

solve(22, 100)
solve(1000, 10000)
solve(100000, 1000000)

for x in range(int(input())):
    n = int(input())
    for i in list:
        if i >= n :
            break
        else:
            print(i, end = " ")
    print()
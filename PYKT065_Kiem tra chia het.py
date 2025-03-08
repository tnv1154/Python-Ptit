

def check(i, n):
    for j in range(2, n):
        if i % j == 0:
            return False
    return True

while True:
    s = input()
    if s == "-1":
        break
    l, r = map(int, s.split())
    n = int(input())
    cnt = 0
    for i in range(l, r + 1):
        if check(i, n):
            cnt += 1
    print(cnt)
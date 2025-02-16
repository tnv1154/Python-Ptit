
for x in range(int(input())):
    n = input()
    ans = int(n)
    ok = False
    if int(n) % 7 == 0:
        print(n)
        continue
    for i in range(1001):
        ans += int(n[::-1])
        n = str(ans)
        if ans  % 7 == 0 :
            ok = True
            print(ans)
            break
    if not ok:
        print("-1")
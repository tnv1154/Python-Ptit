
def tsnto(n):
    mp = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            if d in mp:
                mp[d] += 1
            else:
                mp[d] = 1
            n //= d
        d += 1
    if n > 1:
        mp[n] = 1
    return mp

def display(mp):
    ans = ["1"]
    for i in sorted(mp.keys()):
        ans.append(f"{i}^{mp[i]}")
    return " * ".join(ans)

for _ in range(int(input())):
    n = int(input())
    mp = tsnto(n)
    print(display(mp))
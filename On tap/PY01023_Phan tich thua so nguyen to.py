
def phantich(s):
    mp = {}
    n = int(s)
    i = 2
    while n > 1:
        if n % i == 0:
            if i not in mp:
                mp[i] = 1
            else:
                mp[i] = mp[i] + 1
            n /= i
        else:
            i += 1
    if n > 1:
        mp[n] += 1
    return mp

for _ in range(int(input())):
    s = input()
    mp = phantich(s)
    print("1 ", end="")
    for k, v in mp.items():
        print(f"* {k}^{v} ", end="")
    print()


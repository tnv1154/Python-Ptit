import re

def main():
    n, m = map(int, input().split())
    mp = {}
    for i in range(n):
        s = input().lower()
        s = re.sub(r'[^a-z0-9]', ' ', s)
        arr = s.split()
        for j in arr:
            if j not in mp.keys():
                mp[j] = 1
            else:
                mp[j] += 1
    arr = sorted(mp.items(), key=lambda x: (-x[1], x[0]))
    for a in arr:
        if a[1] >= m:
            print(a[0] , a[1])


if __name__ == "__main__":
    main()

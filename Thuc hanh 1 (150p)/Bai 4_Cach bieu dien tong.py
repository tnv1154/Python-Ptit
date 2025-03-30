
def dem(n):
    cnt = 0
    for length in range(2, int((2 * n) ** 0.5) + 1):
        if (2 * n) % length == 0:
            start = (2 * n // length - length + 1) //2
            if start > 0 and (2 * n // length - length + 1) % 2 == 0:
                cnt += 1
    return cnt

for _ in range(int(input())):
    n = int(input())
    print(dem(n))
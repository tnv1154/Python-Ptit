import math

for x in range(int(input())):
    s = input()
    reverse_s = s[::-1]
    s = int(s)
    reverse_s = int(reverse_s)
    if math.gcd(s, reverse_s) == 1:
        print("YES")
    else:
        print("NO")
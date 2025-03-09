
s1 = input()
s2 = input()
k = int(input())
ans = ""
ans = s1[0:k-1] + s2 + s1[k-1:]
print(ans)

